import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[
    [
        "reaction_time_mean",
        "reaction_time_std",
        "reading_wpm",
        "regressions",
        "phoneme_errors",
        "weber_fraction",
        "math_decay",
        "switch_latency"
    ]
]

# Labels (multi-output)
y = data[["adhd", "dyslexia", "dyscalculia"]]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Evaluate
pred = model.predict(X_test)
print(classification_report(y_test, pred))

# Save model
joblib.dump(model, "learning_risk_model.pkl")

print("✅ Model trained and saved")
