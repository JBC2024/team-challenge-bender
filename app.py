import flask
import os

import endpoint_home

# os.chdir(os.path.dirname(__file__))

app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Enruta la landing page (endpoint /)
@app.route('/', methods=['GET'])
def home():
    return endpoint_home.function()

# Enruta la funcion al endpoint /api/v1/predict

# Enruta la funcion al endpoint /api/v1/retrain

# Enruta la funcion al endpoint /api/v1/opcional

debug = False
if __name__ == "__mmain__":
    debug=True

app.run(debug=debug, host='0.0.0.0', port=8080)