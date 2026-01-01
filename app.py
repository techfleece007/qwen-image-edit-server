import io
import torch
from typing import List
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import Response
from diffusers import QwenImageEditPipeline
from PIL import Image

app = FastAPI()
pipe = None

@app.on_event("startup")
async def load_model():
    global pipe

    model_id = "Qwen/Qwen-Image-Edit-Plus"

    pipe = QwenImageEditPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        safety_checker=None,
        requires_safety_checker=False,
        low_cpu_mem_usage=True
    )

    pipe.to("cuda")
    pipe.enable_attention_slicing()
    pipe.safety_checker = None
    pipe.feature_extractor = None

@app.post("/edit")
async def edit_image(
    prompt: str = Form(...),
    images: List[UploadFile] = File(...)
):
    if not images or len(images) < 1:
        raise HTTPException(status_code=400, detail="At least one image required")

    pil_images = []
    for img in images:
        data = await img.read()
        pil_images.append(Image.open(io.BytesIO(data)).convert("RGB"))

    try:
        with torch.no_grad():
            result = pipe(
                prompt=prompt,
                image=pil_images if len(pil_images) > 1 else pil_images[0],
                num_inference_steps=20,
                guidance_scale=7.5
            )

        out = result.images[0]
        buf = io.BytesIO()
        out.save(buf, format="PNG")

        return Response(content=buf.getvalue(), media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
