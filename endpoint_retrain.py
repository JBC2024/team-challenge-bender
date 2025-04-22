from flask import jsonify, request
import pandas as pd
import os
import joblib
import sys
sys.path.insert(0, './')
import utils.common as cm

def function():
    file_name = ""
    if 'file' in request.args and request.args['file'] != '':
        file_name = request.args['file']

        path = f"data/{file_name}.csv"

        if os.path.exists(path):
            new_data = cm.get_dataframe(path)
            target = 'fuel_comb_mpg'
            y_new_data = new_data[target]

            # Cargamos el modelo
            modelo = joblib.load("model.joblib")

            # Reentrenamiento
            modelo.fit(new_data, y_new_data)
            joblib.dump("model.joblib")
            print('\nEl modelo se ha entrenado\n')

            return jsonify(f'El modelo ha sido reentrenado con el archivo {file_name}')
        
        else:
            return jsonify("Error: No se ha encontrado el archivo")
    else:
        return jsonify("Error: No se ha especificado el nombre del archivo")