from typing import Union
from fastapi import FastAPI,UploadFile,File,Request
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )

templates = Jinja2Templates(directory="templates")

#load model 
processor = TrOCRProcessor.from_pretrained("E:\ICBT\DigitRecognizer\model")
model = VisionEncoderDecoderModel.from_pretrained("E:\ICBT\DigitRecognizer\model")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file).convert("RGB")

        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        return {"result": generated_text}
    
    except Exception as e:
        return {"error": str(e)}