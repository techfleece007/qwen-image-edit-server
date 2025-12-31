# Qwen Image Edit Server

Personal-use GPU server for Qwen Image Editing (uncensored).

## API

POST /edit  
Content-Type: multipart/form-data  

- prompt: string  
- image: file (PNG/JPG)  

Returns:  
```json
{"image_base64": "..."}
