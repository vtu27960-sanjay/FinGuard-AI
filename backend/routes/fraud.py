from fastapi import APIRouter
from services.fraud_service import predict_transaction

router = APIRouter()

@router.post("/predict")
def predict(data: dict):

    result = predict_transaction(data)

    if result == 1:
        return {
            "prediction": "Fraud",
            "risk_score": 0.98
        }

    return {
        "prediction": "Safe",
        "risk_score": 0.02
    }