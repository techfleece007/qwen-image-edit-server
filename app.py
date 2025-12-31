from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from diffusers import QwenImageEditPipeline
from PIL import Image
import torch
from io import BytesIO
import base64

app = FastAPI(title="Qwen Image Edit Server")

# Load model
pipe = QwenImageEditPipeline.from_pretrained(
    "Qwen/Qwen-Image-Edit",
    torch_dtype=torch.float16
)
pipe.to("cuda")  # GPU required

@app.post("/edit")
async def edit_image(
    prompt: str = Form(...),
    image: UploadFile = File(...)
):
    try:
        img = Image.open(image.file).convert("RGB")

        result = pipe(
            image=img,
            prompt=prompt,
            num_inference_steps=30,
            guidance_scale=7.5
        )

        output = result.images[0]
        buf = BytesIO()
        output.save(buf, format="PNG")
        encoded = base64.b64encode(buf.getvalue()).decode()

        return JSONResponse({"image_base64": encoded})
    except Exception as e:
        return JSONResponse({"error": str(e)})
