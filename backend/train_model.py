import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("dataset.csv")

X = data[[
    "reaction_time_mean","reaction_time_std","reading_wpm",
    "regressions","phoneme_errors","weber_fraction",
    "math_decay","switch_latency"
]]

y = data[["adhd","dyslexia","dyscalculia"]]

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

joblib.dump(model, "learning_risk_model.pkl")
print("✅ Model trained")
