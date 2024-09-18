# app/model_handlers/sklearn.py
import pickle
import numpy as np

MODEL_PATH = 'models/your_model.pkl'
model = pickle.load(open(MODEL_PATH, 'rb'))

def predict(data):
    # Assuming data is in a suitable format for Scikit-learn
    input_data = np.array([data])
    predictions = model.predict(input_data)
    return {"predictions": predictions.tolist()}
