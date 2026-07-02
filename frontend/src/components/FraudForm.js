import React, { useState } from "react";
import API from "../services/api";

function FraudForm() {
    const [formData, setFormData] = useState({
        amount: "",
        transaction_hour: "",
        merchant_category: "Food",
        foreign_transaction: 0,
        location_mismatch: 0,
        device_trust_score: "",
        velocity_last_24h: "",
        cardholder_age: ""
    });

    const [result, setResult] = useState("");

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const predictFraud = async () => {
        try {
            const response = await API.post("/predict", formData);
            setResult(response.data.prediction);
        } catch (error) {
            console.error(error);
            alert("Prediction Failed");
        }
    };

    return (
        <div className="card p-4 mt-4">
            <h3>Fraud Detection</h3>

            <input
                className="form-control mt-2"
                placeholder="Amount"
                name="amount"
                onChange={handleChange}
            />

            <input
                className="form-control mt-2"
                placeholder="Transaction Hour"
                name="transaction_hour"
                onChange={handleChange}
            />

            <input
                className="form-control mt-2"
                placeholder="Device Trust Score"
                name="device_trust_score"
                onChange={handleChange}
            />

            <input
                className="form-control mt-2"
                placeholder="Velocity Last 24 Hours"
                name="velocity_last_24h"
                onChange={handleChange}
            />

            <input
                className="form-control mt-2"
                placeholder="Cardholder Age"
                name="cardholder_age"
                onChange={handleChange}
            />

            <button
                className="btn btn-primary mt-3"
                onClick={predictFraud}
            >
                Predict
            </button>

            <h4 className="mt-4">
                Prediction: {result}
            </h4>
        </div>
    );
}

export default FraudForm;