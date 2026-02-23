from pydantic import BaseModel, Field
from typing import List, Optional


class PredictionRequest(BaseModel):
    user_id: str = Field(..., example="196")
    movie_id: str = Field(..., example="242")


class PredictionResponse(BaseModel):
    user_id: str
    movie_id: str
    predicted_rating: float
    model_version: str


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool