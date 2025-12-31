# Qwen Image Edit Server

Personal-use GPU server for Qwen Image Editing.

## API

**Endpoint**

POST `/edit`  
Content-Type: `multipart/form-data`

**Fields**

- `prompt`: string  
- `image`: file (PNG/JPG)

**Response**

```json
{
  "image_base64": "..."
}
