import joblib
import numpy as np

# Load trained model & encoders
model = joblib.load("prediction/ml_model.pkl")
label_encoders = joblib.load("prediction/label_encoders.pkl")

# Ensure feature order is consistent
feature_columns = ["Soil Type", "Rock Type", "Rainfall", "Temperature", "Humidity", "Drilling Technique"]

def predict_well_suitability(soil, rock, rainfall, temp, humidity, drilling):
    try:
        # Handle unseen categorical values
        def encode_label(label, category):
            if label in label_encoders[category].classes_:
                return label_encoders[category].transform([label])[0]
            else:
                print(f"⚠ Warning: Unseen label '{label}' in {category}, using default.")
                return 0  # Default to first category

        # Encode categorical features
        soil_encoded = encode_label(soil, "Soil Type")
        rock_encoded = encode_label(rock, "Rock Type")
        drilling_encoded = encode_label(drilling, "Drilling Technique")

        # Ensure feature consistency
        features = np.array([[soil_encoded, rock_encoded, rainfall, temp, humidity, drilling_encoded]])

        # Check feature count
        print(f"Feature count: {features.shape[1]} (Expected: {len(feature_columns)})")

        # Make prediction
        prediction = model.predict(features)

        # Extract results
        well_suitability = "Suitable" if prediction[0][0] > 0.5 else "Not Suitable"
        depth = round(prediction[0][1], 2)
        discharge = round(prediction[0][2], 2)

        print(f"Prediction: {prediction}")

        return {
            "Well_Suitability": well_suitability,
            "Depth": depth,
            "Discharge": discharge,
        }
    except Exception as e:
        print(f"❌ Prediction Error: {e}")
        return {"error": str(e)}





