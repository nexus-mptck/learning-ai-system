from fastapi import FastAPI
from pydantic import BaseModel
from model import predict

app = FastAPI(title="Learning Risk Backend")

class Metrics(BaseModel):
    reaction_time_mean: float
    reaction_time_std: float
    reading_wpm: float
    regressions: int
    phoneme_errors: int
    weber_fraction: float
    math_decay: float
    switch_latency: float

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/analyze")
def analyze(data: Metrics):
    features = [
        data.reaction_time_mean,
        data.reaction_time_std,
        data.reading_wpm,
        data.regressions,
        data.phoneme_errors,
        data.weber_fraction,
        data.math_decay,
        data.switch_latency
    ]

    pred = predict(features)

    return {
        "ADHD": "High" if pred[0] else "Low",
        "Dyslexia": "High" if pred[1] else "Low",
        "Dyscalculia": "High" if pred[2] else "Low"
    }
