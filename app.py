import flask
import os
import sys

sys.path.insert(0, './')
import utils.common

import endpoint_home
import endpoint_prediction
import endpoint_redespliegue
import endpoint_retrain

# os.chdir(os.path.dirname(__file__))

app = flask.Flask(__name__)
# app.config['DEBUG'] = True

# Enruta la landing page (endpoint /)
@app.route('/', methods = ['GET'])
def home():
    return endpoint_home.function()

# Enruta la funcion al endpoint /api/v1/predict
@app.route('/api/v1/predict', methods = ['POST'])
def predict():
    return endpoint_prediction.function()

# Enruta la funcion al endpoint /api/v1/redeploy
@app.route('/api/v1/redeploy', methods = ['POST'])
def redeploy():
    return endpoint_redespliegue.redeploy()

# Enruta la funcion al endpoint /api/v1/retrain
@app.route('/api/v1/retrain', methods = ['GET'])
def retrain():
    return endpoint_retrain.function()

debug = False
if __name__ == "__mmain__":
    debug = True

app.run(debug=debug, host='0.0.0.0', port=8080)