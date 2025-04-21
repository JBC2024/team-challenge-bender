# Team Challenge Bender – API de Predicción

Este repositorio forma parte de un team challenge y nuestro objetivo ha sido crear una API REST capaz de realizar predicciones a partir de un modelo de Machine Learning, que además esté disponible online para cualquier persona.

La API está desplegada públicamente y lista para recibir peticiones y devolver respuestas. 

---

## ¿Dónde está publicada?

Accede a nuestra API desde esta URL:  [https://team-challenge-bender.onrender.com/](https://team-challenge-bender.onrender.com/)



## Endpoints disponibles:

Hemos preparado varios "endpoints".  

| Endpoint        | ¿Para qué sirve?                                                                                              |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| `/`             | Página principal. Te explica cómo funciona la API.          |
| `/predict`      | Envías datos y recibes una predicción del modelo.                                                             |
| `/retrain`      | Permite reentrenar el modelo con nuevos datos.  |

---

## ¿Qué predice el modelo?
El modelo está entrenado para predecir el valor de `fuel_comb_mpg`, es decir, el **consumo combinado del vehículo en millas por galón (MPG)**, usando datos como motor, combustible, tipo de coche, etc.

---

## ¿Cómo lo uso desde Python?

Se puede acceder a él con la librería `requests`:

```python
import requests
url = "https://team-challenge-bender.onrender.com/api/v1/predict"

data = {
    "year": 2020,
    "brand": "Toyota",
    "model": "Corolla",
    "vehicle_class": "Compact",
    "engine_size": 2.0,
    "cylinders": 4,
    "transmission": "Automatic",
    "fuel_type": "Gasoline",
    "fuel_city_Lkm": 7.1,
    "fuel_hwy_Lkm": 5.5,
    "co2": 150
}

response = requests.post(url, json=data)
print(response.json())

