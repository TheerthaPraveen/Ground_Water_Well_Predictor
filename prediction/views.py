from django.shortcuts import render
from .ml_model import predict_well_suitability

def index(request):
    return render(request, 'prediction/index.html')

def predict(request):
    if request.method == "POST":
        soil = request.POST["soil_type"]
        rock = request.POST["rock_type"]
        rainfall = float(request.POST["rainfall"])
        temp = float(request.POST["temperature"])
        humidity = float(request.POST["humidity"])
        drilling = request.POST["drilling_technique"]

        # Get predictions from ML model
        result = predict_well_suitability(soil, rock, rainfall, temp, humidity, drilling)

        # Debugging output
        print("Prediction Result:", result)

        return render(request, "prediction/predict.html", {"result": result})

    return render(request, "prediction/predict.html")
