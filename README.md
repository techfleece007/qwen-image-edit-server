# Qwen Image Edit Plus - Backend Server

FastAPI backend server for Qwen Image Edit Plus model, deployed on Koyeb with GPU support.

## Tech Stack

- **FastAPI** - Modern Python web framework
- **Diffusers** - Hugging Face library for diffusion models
- **PyTorch** - Deep learning framework
- **CUDA** - GPU acceleration

## Features

- Supports Qwen Image Edit Plus model
- Accepts one or two input images
- Text prompt-based image editing
- Safety checker disabled for unrestricted generation
- GPU-accelerated inference

## API Endpoint

### POST `/edit`

Accepts multipart/form-data with:
- `prompt` (string, required) - Text description of desired edits
- `image1` (file, required) - First input image (PNG/JPG)
- `image2` (file, optional) - Second input image (PNG/JPG)

**Response:**
```json
{
  "image_base64": "base64_encoded_image_string"
}
```

## Local Development

### Prerequisites

- Python 3.10+
- CUDA-capable GPU with 24GB+ VRAM
- NVIDIA drivers installed

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The model will be downloaded automatically on first run (~5-10 minutes).

## Deployment on Koyeb

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy

```bash
koyeb app init qwen-image-edit \
  --git https://github.com/your-username/qwen-image-edit-server \
  --instance-type gpu-nvidia-a100 \
  --regions iow \
  --port 8000:http \
  --route /:8000
```

### Recommended GPU

- **NVIDIA A100** (80GB VRAM) - Best performance
- **NVIDIA L40S** (48GB VRAM) - Cost-effective
- **NVIDIA L4** (24GB VRAM) - Minimum recommended

### Recommended Region

- **Iowa (IOW)** - For A100 SXM
- **Dallas (DAL)** - For A100/H100
- Any region for L4/L40S (choose closest to users)

## Model Information

- **Model:** `Qwen/Qwen-Image-Edit-Plus`
- **VRAM Required:** Minimum 24GB (L4), Recommended 48GB+ (L40S/A100)
- **Safety Checker:** Disabled in this implementation

## Project Structure

```
.
├── app.py                 # FastAPI application
├── Dockerfile             # Container configuration
├── requirements.txt       # Python dependencies
├── DEPLOYMENT.md         # Koyeb deployment guide
├── IMPLEMENTATION_NOTES.md # Technical details
└── README.md             # This file
```

## Environment Variables

No environment variables required for basic setup. The model is downloaded automatically.

## Testing

### Test with single image:
```bash
curl -X POST http://localhost:8000/edit \
  -F "prompt=Make the image more vibrant" \
  -F "image1=@test_image.jpg"
```

### Test with two images:
```bash
curl -X POST http://localhost:8000/edit \
  -F "prompt=Combine elements from both images" \
  -F "image1=@image1.jpg" \
  -F "image2=@image2.jpg"
```

## Important Notes

⚠️ **Safety Checker Disabled:** This implementation has safety filtering disabled. Use responsibly.

⚠️ **First Request:** The first request may be slow as the model initializes.

⚠️ **Cold Starts:** With scale-to-zero enabled, expect delays when scaling up.

## Troubleshooting

- **Out of Memory:** Use A100 instead of L4
- **Model Not Found:** Ensure diffusers version is >= 0.27.2
- **Slow Inference:** Verify GPU is being used
- **Connection Errors:** Check port 8000 is correctly configured

## License


Personal use only.
