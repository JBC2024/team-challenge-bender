from flask import jsonify, request
import pandas as pd
import os
import joblib

def function():
    file_name = ""
    if 'file' in request.args:
        file_name = request.args['file']

        path = f"data/{file_name}.csv"

        if os.path.exists(path):
            new_data = pd.read_csv(path)
                
            # Cargamos el modelo
            modelo = joblib.load("model.joblib")

            # Reentrenamiento
            modelo.fit(new_data)
            joblib.dump("model.joblib")

            return jsonify(f'El modelo ha sido reentrenado con el archivo {file_name}')
        
        else:
            return jsonify("Error: No se ha encontrado el archivo")
    else:
        return jsonify("Error: No se ha especificado el nombre del archivo")