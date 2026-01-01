from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from PIL import Image
import torch
from io import BytesIO
import base64
from typing import Optional

# Workaround for torch.xpu AttributeError in diffuserss
# Some versions of diffusers try to access torch.xpu which doesn't exist in standard PyTorch
# This creates a complete mock of torch.xpu with all expected attributes
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
    
    torch.xpu = XPUModule()

from diffusers import QwenImageEditPipeline

app = FastAPI(title="Qwen Image Edit Plus Server")

# Load model once at startup
pipe = QwenImageEditPipeline.from_pretrained(
    "Qwen/Qwen-Image-Edit-Plus",
    torch_dtype=torch.float16,
)
pipe.to("cuda")  # Ensure GPU usage

# Disable safety checker if it exists
if hasattr(pipe, 'safety_checker'):
    pipe.safety_checker = None
if hasattr(pipe, 'feature_extractor'):
    pipe.feature_extractor = None


@app.post("/edit")
async def edit_image(
    prompt: str = Form(...),
    image1: UploadFile = File(...),
    image2: Optional[UploadFile] = File(None),
):
    try:
        # Read and load first image (required)
        img1_bytes = await image1.read()
        img1 = Image.open(BytesIO(img1_bytes)).convert("RGB")
        
        # Prepare images list
        images = [img1]
        
        # Add second image if provided
        if image2:
            img2_bytes = await image2.read()
            img2 = Image.open(BytesIO(img2_bytes)).convert("RGB")
            images.append(img2)

        # Run inference
        # Qwen Image Edit Plus supports multiple images
        # If pipeline doesn't accept list, it will use the first image
        # Try passing list first, fallback to single image if needed
        try:
            if len(images) > 1:
                # Multiple images: pass as list
                result = pipe(
                    image=images,
                    prompt=prompt,
                    num_inference_steps=30,
                    guidance_scale=7.5,
                )
            else:
                # Single image
                result = pipe(
                    image=images[0],
                    prompt=prompt,
                    num_inference_steps=30,
                    guidance_scale=7.5,
                )
        except TypeError:
            # Fallback: if pipeline doesn't support list, use first image only
            result = pipe(
                image=images[0],
                prompt=prompt,
                num_inference_steps=30,
                guidance_scale=7.5,
            )

        output = result.images[0]

        # Encode result as base64 PNG
        buf = BytesIO()
        output.save(buf, format="PNG")
        encoded = base64.b64encode(buf.getvalue()).decode("utf-8")

        return JSONResponse({"image_base64": encoded})

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error: {error_details}")
        return JSONResponse({"error": str(e)}, status_code=500)
