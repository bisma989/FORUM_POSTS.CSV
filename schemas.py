from pydantic import BaseModel, Field

class SentimentRequest(BaseModel):
    text: str = Field(..., description="The post text to analyze", example="I love this product!")

class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    confidence: float