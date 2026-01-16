import joblib
from core.config import MODEL_PATH

model = joblib.load(MODEL_PATH)

def predict_risk(features):
    prediction = model.predict([features])[0]
    probabilities = model.predict_proba([features])
    return prediction, probabilities
