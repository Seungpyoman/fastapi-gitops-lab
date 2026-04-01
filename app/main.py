from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Inference API Demo")

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
MODEL_NAME = os.getenv("MODEL_NAME", "rule-based-demo")


class PredictRequest(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {
        "message": "FastAPI Inference API is running",
        "version": APP_VERSION,
        "model": MODEL_NAME
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {
        "version": APP_VERSION,
        "model": MODEL_NAME
    }


@app.post("/predict")
def predict(request: PredictRequest):
    text = request.text.lower()

    if "error" in text or "fail" in text:
        prediction = "abnormal"
    else:
        prediction = "normal"

    return {
        "input": request.text,
        "prediction": prediction,
        "model": MODEL_NAME,
        "version": APP_VERSION
    }