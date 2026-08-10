import os
import joblib

class SentimentModelService:
    def __init__(self, model_path: str = "models/sentiment_model.pkl"):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        """Loads the trained machine learning model from disk safely."""
        try:
            if os.path.exists(self.model_path) and os.path.getsize(self.model_path) > 0:
                return joblib.load(self.model_path)
        except Exception:
            pass
        return None  # Fallback to mock prediction logic if file is empty or missing

    def predict(self, text: str) -> dict:
        """Runs inference on the input text."""
        if self.model is None:
            # Fallback logic if no model file is loaded properly
            sentiment = "Positive" if any(word in text.lower() for word in ["good", "love", "great", "awesome", "happy"]) else "Negative"
            confidence = 0.85
            return {"sentiment": sentiment, "confidence": confidence}

        # Real model prediction logic (if a valid sklearn pipeline is loaded)
        prediction = self.model.predict([text])[0]
        probabilities = self.model.predict_proba([text])[0]
        confidence = float(max(probabilities))
        return {"sentiment": str(prediction), "confidence": confidence}

# Singleton instance to avoid reloading the model on every request
model_service = SentimentModelService()