import torch
from fastapi import FastAPI, UploadFile, Form
from diffusers import DiffusionPipeline
from PIL import Image
import io

app = FastAPI()

pipe = DiffusionPipeline.from_pretrained(
    "Qwen/Qwen-Image-Edit",
    torch_dtype=torch.float16,
    trust_remote_code=True
).to("cuda")

@app.post("/edit")
async def edit_image(
    image: UploadFile,
    prompt: str = Form(...)
):
    image_bytes = await image.read()
    init_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    result = pipe(
        prompt=prompt,
        image=init_image
    ).images[0]

    buf = io.BytesIO()
    result.save(buf, format="PNG")
    buf.seek(0)

    return {
        "status": "success",
    }
