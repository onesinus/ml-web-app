# ML Web Application with FastAPI and Docker Compose

This project is a web application that serves machine learning models in various formats (TensorFlow, PyTorch, Scikit-learn, ONNX). The application is built with **FastAPI** and Dockerized for easy deployment.

## Features
- Serve multiple machine learning model formats:
  - TensorFlow (`.h5`)
  - PyTorch (`.pth`)
  - Scikit-learn (`.pkl`)
  - ONNX (`.onnx`)
- Containerized with **Docker** and **Docker Compose**
- Scalable and modular architecture for adding more model formats

## Project Structure

```
ml-web-app/
│
├── app/                   # FastAPI application
│   ├── main.py            # FastAPI app entry point
│   ├── model_handlers/     # Handlers for different ML models
│   │   ├── tensorflow.py   # TensorFlow model handling
│   │   ├── pytorch.py      # PyTorch model handling
│   │   ├── sklearn.py      # Scikit-learn model handling
│   │   └── onnx.py         # ONNX model handling
│   └── requirements.txt    # Dependencies
│
├── models/                # Directory to store models
│   ├── your_model.h5       # Example TensorFlow model
│   └── your_model.pth      # Example PyTorch model
│
├── Dockerfile             # Dockerfile for FastAPI
├── docker-compose.yml     # Docker Compose file
└── README.md              # Instructions
```

## Setup and Installation

### Prerequisites
Make sure you have the following installed:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ml-web-app.git
   cd ml-web-app
   ```

2. Place your models in the `models/` directory. For example:
   - TensorFlow model (`your_model.h5`)
   - PyTorch model (`your_model.pth`)
   - Scikit-learn model (`your_model.pkl`)
   - ONNX model (`your_model.onnx`)

3. Build the Docker containers:
   ```bash
   docker-compose build
   ```

4. Run the application:
   ```bash
   docker-compose up
   ```

   OR

   ```bash
   docker-compose up -d
   ```

The FastAPI web server will be available at `http://localhost:5000`.

### API Endpoints

#### 1. **Root Endpoint**
```bash
GET / 
```
Returns a welcome message.

#### 2. **Model Prediction Endpoint**
```bash
POST /predict/{model_type}
```
- `model_type`: The type of model you want to use (`tensorflow`, `pytorch`, `sklearn`, or `onnx`).

##### Example Request (using `curl`):
```bash
curl -X POST "http://localhost:5000/predict/tensorflow" \
    -H "accept: application/json" \
    -H "Content-Type: multipart/form-data" \
    -F "file=@input.json"
```

### Adding New Models
To add a new model, simply place it in the `models/` directory and ensure the correct model format is used for the handler.

### Logs and Debugging
You can view the logs for each service using the following command:
```bash
docker-compose logs -f
```

## Example Input Format
- The input to the models should be in a format compatible with the model. Typically, this will be a JSON or file upload. Ensure the input matches the expected input shape of your specific model.

## Known Issues
- Input data format: Make sure that the input data is preprocessed correctly and matches the expected format for each model type.

## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork this project and open a pull request if you'd like to contribute!
```