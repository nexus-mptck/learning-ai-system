import joblib

model = joblib.load("learning_risk_model.pkl")

def predict(features):
    return model.predict([features])[0]
