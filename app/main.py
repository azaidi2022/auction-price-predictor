from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_spread

app = FastAPI(title="Auction Car Spread Predictor")


class CarInput(BaseModel):
    year: int
    make: str
    model: str
    trim: str
    body: str
    transmission: str
    state: str
    odometer: float
    condition: float
    color: str
    interior: str
    saledate: str
    mmr: float


@app.get("/")
def root():
    return {"message": "Auction Car Spread Predictor API is running"}


@app.post("/predict")
def predict(data: CarInput):
    payload = data.model_dump()

    predicted_spread = predict_spread(payload)
    estimated_price = payload["mmr"] + predicted_spread

    return {
        "predicted_spread": round(predicted_spread, 2),
        "mmr": round(payload["mmr"], 2),
        "estimated_sale_price": round(estimated_price, 2),
    }
