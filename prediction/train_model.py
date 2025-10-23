import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("water_well_prediction_large_dataset.csv")

# ✅ Rename columns to match expected names
df.rename(columns={
    'Rainfall (mm/year)': 'Rainfall',
    'Temperature (°C)': 'Temperature',
    'Humidity (%)': 'Humidity',
    'Depth (m)': 'Depth',  # Fixing column names
    'Discharge (liters/sec)': 'Discharge'
}, inplace=True)

# 🔹 Print column names after renaming (debugging)
print("Updated Dataset Columns:", df.columns)

# Identify categorical columns
categorical_columns = ["Soil Type", "Rock Type", "Drilling Technique"]
label_encoders = {}

# 🔹 Encode categorical columns
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 🔹 Convert "Well Suitability" to numerical (0 = Not Suitable, 1 = Suitable)
le_suitability = LabelEncoder()
df["Well Suitability"] = le_suitability.fit_transform(df["Well Suitability"])
label_encoders["Well Suitability"] = le_suitability

# 🔹 Define input (features) and output (targets)
feature_columns = ["Soil Type", "Rock Type", "Rainfall", "Temperature", "Humidity", "Drilling Technique"]
target_columns = ["Well Suitability", "Depth", "Discharge"]  # ✅ Now these match exactly

# Extract input features and target
X = df[feature_columns]  
Y = df[target_columns]

# Split dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# Save trained model and encoders
joblib.dump(model, "prediction/ml_model.pkl")
joblib.dump(label_encoders, "prediction/label_encoders.pkl")

print("✅ Model training complete. Model and encoders saved!")
