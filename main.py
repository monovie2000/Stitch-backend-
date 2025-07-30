import requests
import os
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse

app = FastAPI()

IMGBB_API_KEY = os.getenv("2cf4a8edbac83b437f965c5d0ac05c63")  # from your environment on Render

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    url = "https://api.imgbb.com/1/upload"
    payload = {
        "key": IMGBB_API_KEY,
        "image": contents.encode("base64") if hasattr(contents, 'encode') else contents
    }
    response = requests.post(url, files={"image": contents}, data={"key": IMGBB_API_KEY})
    
    if response.status_code == 200:
        image_url = response.json()['data']['url']
        return {"image_url": image_url}
    else:
        return JSONResponse(content={"error": response.text}, status_code=400)