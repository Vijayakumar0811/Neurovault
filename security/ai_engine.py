import joblib
import os

# Get absolute path to the model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "neurovault_ai.pkl")

# Load the AI model
model = joblib.load(MODEL_PATH)

def predict(features):
    prob = model.predict_proba([features])[0][1]
    return {
        "risk_score": float(prob),
        "is_attack": bool(prob > 0.6),
        "confidence": round(prob * 100, 2)
    }