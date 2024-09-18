# app/model_handlers/tensorflow.py
import tensorflow as tf
import numpy as np

MODEL_PATH = 'models/your_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

def predict(data):
    # Assuming data is in a suitable format for TensorFlow (e.g., JSON or numpy array)
    input_data = np.array([data])  # Adjust as necessary
    predictions = model.predict(input_data)
    return {"predictions": predictions.tolist()}
