import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Crear app
app = FastAPI()

# Cargar modelo entrenado
model = joblib.load("models/random_forest_model.pkl")

# Definir estructura de datos de entrada
class WineInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float


@app.get("/")
def home():
    return {"mensaje": "API del modelo funcionando correctamente"}


@app.post("/predict")
def predict(data: WineInput):
    
    # Convertir a DataFrame
    df = pd.DataFrame([data.dict()])
    
    # Ajustar nombres si en tu dataset tienen espacios
    df.columns = [
        "fixed acidity",
        "volatile acidity",
        "citric acid",
        "residual sugar",
        "chlorides",
        "free sulfur dioxide",
        "total sulfur dioxide",
        "density",
        "pH",
        "sulphates",
        "alcohol"
    ]
    
    prediction = model.predict(df)[0]
    
    return {"prediction": int(prediction)}