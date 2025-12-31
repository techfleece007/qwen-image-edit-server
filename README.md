# Qwen Image Edit Server

## Description
Personal-use server for Qwen Image Editing. Fully uncensored.

## API
POST /edit  
Content-Type: multipart/form-data  
Fields:
- prompt: string
- image: file (PNG/JPG)

Response:
```json
{"image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."}
