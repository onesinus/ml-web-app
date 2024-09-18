# app/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies (less likely to change frequently)
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]