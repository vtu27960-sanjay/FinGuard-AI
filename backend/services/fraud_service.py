import joblib
import pandas as pd
from database.db import get_connection

# Load trained model
model = joblib.load("../models/fraud_model.pkl")

def predict_transaction(data):

    df = pd.DataFrame([data])

    # Convert merchant category to number
    category_map = {
        "Food": 0,
        "Travel": 1,
        "Shopping": 2,
        "Entertainment": 3,
        "Bills": 4,
        "Healthcare": 5,
        "Others": 6
    }

    if "merchant_category" in df.columns:
        df["merchant_category"] = df["merchant_category"].map(category_map).fillna(6)

    prediction = model.predict(df)[0]

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO transactions
    (
        amount,
        transaction_hour,
        merchant_category,
        foreign_transaction,
        location_mismatch,
        device_trust_score,
        velocity_last_24h,
        cardholder_age,
        prediction
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        data["amount"],
        data["transaction_hour"],
        data["merchant_category"],
        data["foreign_transaction"],
        data["location_mismatch"],
        data["device_trust_score"],
        data["velocity_last_24h"],
        data["cardholder_age"],
        "Fraud" if prediction == 1 else "Safe"
    )

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    return prediction