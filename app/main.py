# app/main.py
from fastapi import FastAPI, UploadFile, File
from app.model_handlers import tensorflow, pytorch, sklearn, onnx
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to ML Model API"}

# Endpoint to upload and process data for each model format
@app.post("/predict/{model_type}")
async def predict(model_type: str, file: UploadFile = File(...)):
    data = await file.read()

    if model_type == 'tensorflow':
        return tensorflow.predict(data)
    elif model_type == 'pytorch':
        return pytorch.predict(data)
    elif model_type == 'sklearn':
        return sklearn.predict(data)
    elif model_type == 'onnx':
        return onnx.predict(data)
    else:
        return {"error": "Unsupported model type"}

