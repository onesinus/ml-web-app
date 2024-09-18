# app/model_handlers/onnx.py
import onnxruntime as rt
import numpy as np

MODEL_PATH = 'models/your_model.onnx'
sess = rt.InferenceSession(MODEL_PATH)

def predict(data):
    input_data = np.array([data])
    input_name = sess.get_inputs()[0].name
    predictions = sess.run(None, {input_name: input_data})[0]
    return {"predictions": predictions.tolist()}
