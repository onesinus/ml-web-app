# app/model_handlers/pytorch.py
import torch
import numpy as np

MODEL_PATH = 'models/your_model.pth'
model = torch.load(MODEL_PATH)
model.eval()

def predict(data):
    # Assuming data is in a suitable format for PyTorch
    input_tensor = torch.tensor(np.array([data]))
    with torch.no_grad():
        predictions = model(input_tensor)
    return {"predictions": predictions.numpy().tolist()}
