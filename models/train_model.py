import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../datasets/creditcard.csv")

print("Dataset Loaded Successfully!")

# Encode merchant_category
encoder = LabelEncoder()
df["merchant_category"] = encoder.fit_transform(df["merchant_category"])

# Remove transaction_id (not useful for prediction)
X = df.drop(columns=["transaction_id", "is_fraud"])

# Target
y = df["is_fraud"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, "fraud_model.pkl")

print("✅ Model trained successfully!")
print("✅ Model saved as fraud_model.pkl")