# Team Challenge Bender – API de Predicción

Este repositorio forma parte de un team challenge y nuestro objetivo ha sido crear una API REST capaz de realizar predicciones a partir de un modelo de Machine Learning, que además esté disponible online para cualquier persona.

La API está desplegada públicamente y lista para recibir peticiones y devolver respuestas. 

---

## ¿Dónde está publicada?

Accede a nuestra API desde esta URL:

https://team-challenge-bender.onrender.com/



## Endpoints disponibles:

Hemos preparado varios "endpoints".  
Un endpoint es como una puerta de entrada a una funcionalidad concreta.

| Endpoint        | ¿Para qué sirve?                                                                                              |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| `/`             | Página principal. Te explica cómo funciona la API.          |
| `/predice`      | Envías datos y recibes una predicción del modelo.                                                             |
| `/entrena`      | Permite reentrenar el modelo con nuevos datos.  |


---

## 🧪 ¿Cómo lo uso desde Python?

Se puede acceder a él  con la librería `requests`:

```python
import requests

# Enviar datos al endpoint /predice
respuesta = requests.get(
    "https://team-challenge-bender.onrender.com/predice",
    params={"dato1": "valor1", "dato2": "valor2"}
)

print(respuesta.json())
