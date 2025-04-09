from flask import Flask, jsonify, request
import os

# os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

# Enruta la landing page (endpoint /)

# Enruta la funcion al endpoint /api/v1/predict

# Enruta la funcion al endpoint /api/v1/retrain

# Ponerlo así para que sirva a la hora de desplegarlo en servidores
if __name__ == "__mmain__"
    app.run(debug=True)
