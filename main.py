from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

IMGBB_API_KEY = "2cf4a8edbac83b437f965c5d0ac05c63"

@app.get("/")
def root():
    return {"message": "👗 Stitch FashionBot is live!"}

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    # Read file and prepare payload
    image_data = await file.read()
    response = requests.post(
        "https://api.imgbb.com/1/upload",
        params={"key": IMGBB_API_KEY},
        files={"image": image_data}
    )

    if response.status_code == 200:
        data = response.json()
        return {
            "success": True,
            "url": data["data"]["url"],
            "display_url": data["data"]["display_url"]
        }
    else:
        return {
            "success": False,
            "error": response.text
        }
