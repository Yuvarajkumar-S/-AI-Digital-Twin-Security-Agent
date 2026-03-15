import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import joblib
import os

DATA_FILE = "user_behavior.csv"
MODEL_FILE = "anomaly_model.pkl"

# create models folder
os.makedirs("models", exist_ok=True)

print("Loading dataset...")

df = pd.read_csv(DATA_FILE)

print("Dataset size:", len(df))


# -------------------------
# Feature Selection
# -------------------------

features = df[[
    "hour",
    "typing_speed",
    "session_duration",
    "apps_used_count"
]]

# -------------------------
# Encode location
# -------------------------

location_encoder = LabelEncoder()
df["location_encoded"] = location_encoder.fit_transform(df["location"])

features["location"] = df["location_encoded"]

# -------------------------
# Train Isolation Forest
# -------------------------

print("Training anomaly detection model...")

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(features)

# -------------------------
# Save Model
# -------------------------

joblib.dump(model, MODEL_FILE)

print("Model trained successfully!")

print("Model saved to:", MODEL_FILE)