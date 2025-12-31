from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from diffusers import QwenImageEditPipeline
from PIL import Image
import torch
from io import BytesIO
import base64

app = FastAPI(title="Qwen Image Edit Server")

# Load model once at startup
pipe = QwenImageEditPipeline.from_pretrained(
    "Qwen/Qwen-Image-Edit",
    torch_dtype=torch.float16,
)
pipe.to("cuda")  # Ensure GPU usage


@app.post("/edit")
async def edit_image(
    prompt: str = Form(...),
    image: UploadFile = File(...),
):
    try:
        # Read and load image
        img_bytes = await image.read()
        img = Image.open(BytesIO(img_bytes)).convert("RGB")

        # Run inference
        result = pipe(
            image=img,
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
        return JSONResponse({"error": str(e)}, status_code=500)
