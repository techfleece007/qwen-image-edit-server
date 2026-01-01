import torch
from fastapi import FastAPI, UploadFile, Form
from diffusers import DiffusionPipeline
from PIL import Image
import io

app = FastAPI()

pipe = DiffusionPipeline.from_pretrained(
    "Qwen/Qwen-Image-Edit",
    custom_pipeline="qwen_image_edit",
    trust_remote_code=True,
    torch_dtype=torch.float16
).to("cuda")

@app.post("/edit")
async def edit_image(
    image: UploadFile,
    prompt: str = Form(...)
):
    image_bytes = await image.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    with torch.no_grad():
        result = pipe(
            prompt=prompt,
            image=image
        ).images[0]

    buf = io.BytesIO()
    result.save(buf, format="PNG")
    buf.seek(0)

    return buf.getvalue()
