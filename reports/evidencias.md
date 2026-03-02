# Documentacion evidencias

*El modelo fue entrenado utilizando un Random Forest y guardado en: models/random_forest_model.pkl

*El entrenamiento se ejecuta con: python src/train.py


## Levantamiento de la API

El modelo fue desplegado como servicio REST utilizando FastAPI.

Para iniciar el servidor se ejecutó el siguiente comando:


uvicorn src.serving:app --reload

La API se ejecuta en: http://127.0.0.1:8000


# Ejemplo de entrada(json)
```json
{
  "fixed_acidity": 7.4,
  "volatile_acidity": 0.7,
  "citric_acid": 0.0,
  "residual_sugar": 1.9,
  "chlorides": 0.076,
  "free_sulfur_dioxide": 11,
  "total_sulfur_dioxide": 34,
  "density": 0.9978,
  "pH": 3.51,
  "sulphates": 0.56,
  "alcohol": 12.4
}
```
 Respuesta
```json
{
  "prediction": 1
}

```
# Donde: 
 * 0 representa vino de baja calidad
 * 1 representa vino de alta calidad

Esto demuestra que el modelo recibe correctamente los datos y los predice.

# Las pruebas se realizaron utilizando:

* Interfaz automática de FastAPI 

* Cliente REST (Postman).