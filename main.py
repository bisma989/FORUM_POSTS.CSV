from fastapi import FastAPI, HTTPException
from app.schemas import SentimentRequest, SentimentResponse
from app.model import model_service

app = FastAPI(
    title="Sentiment Analysis Microservice",
    description="AI Internees Week 7 Task: Turning a sentiment model into a FastAPI endpoint.",
    version="1.0.0"
)

@app.get("/", tags=["Health Check"])
def read_root():
    return {"message": "Welcome to the Sentiment Analysis API! Head over to /docs for interactive testing."}

@app.post("/predict", response_model=SentimentResponse, tags=["Prediction"])
def predict_sentiment(payload: SentimentRequest):
    """
    Endpoint to predict sentiment from post text.
    - **text**: The body of the post you want analyzed.
    """
    try:
        result = model_service.predict(payload.text)
        return {
            "text": payload.text,
            "sentiment": result["sentiment"],
            "confidence": result["confidence"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {str(e)}")