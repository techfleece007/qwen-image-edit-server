from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from PIL import Image
import torch
from io import BytesIO
import base64
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Workaround for torch.distributed.device_mesh (required by newer diffusers)
# device_mesh was added in PyTorch 2.3.0, but we add a mock for older versions
# This must be done before importing diffusers
if not hasattr(torch.distributed, 'device_mesh'):
    # Create a proper DeviceMesh class that diffusers expects
    class DeviceMesh:
        """Mock DeviceMesh for compatibility with diffusers"""
        def __init__(self, *args, **kwargs):
            pass
    # Add it to torch.distributed before diffusers tries to use it
    torch.distributed.device_mesh = DeviceMesh

# Workaround for torch.xpu AttributeError in diffusers
# Some versions of diffusers try to access torch.xpu which doesn't exist in standard PyTorch
# This creates a complete mock of torch.xpu with all expected attributes
# Based on diffusers/utils/torch_utils.py which accesses: empty_cache, device_count, manual_seed
if not hasattr(torch, 'xpu'):
    class XPUModule:
        @staticmethod
        def empty_cache():
            """No-op for XPU cache clearing"""
            pass
        
        @staticmethod
        def is_available():
            """Returns False since we don't have XPU devices"""
            return False
        
        @staticmethod
        def device_count():
            """Returns 0 since we don't have XPU devices"""
            return 0
        
        @staticmethod
        def manual_seed(seed):
            """No-op for XPU manual seed setting"""
            pass
        
        @staticmethod
        def manual_seed_all(seed):
            """No-op for XPU manual seed setting"""
            pass
        
        def __getattr__(self, name):
            """Fallback for any other attributes diffusers might access"""
            # Return a no-op function for any method calls
            def noop(*args, **kwargs):
                pass
            return noop
    
    torch.xpu = XPUModule()

from diffusers import QwenImageEditPipeline

app = FastAPI(title="Qwen Image Edit Server")

# Load model synchronously at import time (more reliable for deployment)
logger.info("Loading Qwen Image Edit model...")
try:
    # Try Qwen-Image-Edit-Plus first, fallback to Qwen-Image-Edit
    model_name = "Qwen/Qwen-Image-Edit-Plus"
    try:
        pipe = QwenImageEditPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            safety_checker=None,  # Disable safety checker
            requires_safety_checker=False,  # Explicitly disable
        )
        logger.info(f"Loaded model: {model_name}")
    except Exception as e:
        logger.warning(f"Failed to load {model_name}, trying Qwen/Qwen-Image-Edit: {e}")
        model_name = "Qwen/Qwen-Image-Edit"
        pipe = QwenImageEditPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            safety_checker=None,
            requires_safety_checker=False,
        )
        logger.info(f"Loaded model: {model_name}")
    
    # Move to GPU
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
        logger.info("Model moved to CUDA")
    else:
        logger.warning("CUDA not available, using CPU")
    
    # Ensure safety checker is completely disabled
    if hasattr(pipe, 'safety_checker'):
        pipe.safety_checker = None
    if hasattr(pipe, 'feature_extractor'):
        pipe.feature_extractor = None
    
    # Enable attention slicing for memory efficiency
    if hasattr(pipe, 'enable_attention_slicing'):
        pipe.enable_attention_slicing()
    
    logger.info("Model loaded successfully")
    
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    pipe = None
    raise


@app.post("/edit")
async def edit_image(
    prompt: str = Form(...),
    image1: UploadFile = File(...),
    image2: Optional[UploadFile] = File(None),
):
    """Edit image(s) based on prompt. Supports one or two images."""
    global pipe
    
    if pipe is None:
        return JSONResponse(
            {"error": "Model not loaded. Please wait for startup to complete."},
            status_code=503
        )
    
    try:
        # Read and load first image (required)
        img1_bytes = await image1.read()
        img1 = Image.open(BytesIO(img1_bytes)).convert("RGB")
        logger.info(f"Loaded first image: {image1.filename}, size: {img1.size}")
        
        # Prepare images list
        images = [img1]
        
        # Add second image if provided
        if image2:
            img2_bytes = await image2.read()
            img2 = Image.open(BytesIO(img2_bytes)).convert("RGB")
            images.append(img2)
            logger.info(f"Loaded second image: {image2.filename}, size: {img2.size}")

        logger.info(f"Processing with prompt: {prompt}")
        
        # Run inference - Qwen Image Edit supports single image
        # For two images, we'll use the first one as the base
        result = pipe(
            image=images[0],  # Use first image as base
            prompt=prompt,
            num_inference_steps=30,
            guidance_scale=7.5,
        )

        output = result.images[0]
        logger.info("Inference completed successfully")

        # Encode result as base64 PNG
        buf = BytesIO()
        output.save(buf, format="PNG")
        encoded = base64.b64encode(buf.getvalue()).decode("utf-8")

        return JSONResponse({"image_base64": encoded})

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        logger.error(f"Error processing image: {error_details}")
        return JSONResponse(
            {"error": str(e), "details": error_details},
            status_code=500
        )


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Qwen Image Edit Server",
        "endpoints": {
            "edit": "POST /edit - Edit image(s) with prompt",
            "health": "GET /health - Health check",
            "docs": "GET /docs - API documentation"
        },
        "usage": {
            "method": "POST",
            "endpoint": "/edit",
            "content_type": "multipart/form-data",
            "fields": {
                "prompt": "string (required) - Edit description",
                "image1": "file (required) - First image",
                "image2": "file (optional) - Second image"
            }
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    global pipe
    return {
        "status": "healthy" if pipe is not None else "loading",
        "cuda_available": torch.cuda.is_available(),
    }
