from fastapi import APIRouter
from core.model_loader import predict_risk

router = APIRouter()

@router.post("/")
def analyze(data: dict):

    features = [
        data["reaction_time_mean"],
        data["reaction_time_std"],
        data["reading_wpm"],
        data["regressions"],
        data["phoneme_errors"],
        data["weber_fraction"],
        data["math_decay"],
        data["switch_latency"]
    ]

    prediction, _ = predict_risk(features)

    return {
        "ADHD": "High" if prediction[0] else "Low",
        "Dyslexia": "High" if prediction[1] else "Low",
        "Dyscalculia": "High" if prediction[2] else "Low"
    }
