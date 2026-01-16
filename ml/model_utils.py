import joblib

MODEL_PATH = "backend/ml/learning_risk_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_risk(features):
    """
    features = [
        reaction_time_mean,
        reaction_time_std,
        reading_wpm,
        regressions,
        phoneme_errors,
        weber_fraction,
        math_decay,
        switch_latency
    ]
    """
    prediction = model.predict([features])[0]
    probabilities = model.predict_proba([features])

    return prediction, probabilities
