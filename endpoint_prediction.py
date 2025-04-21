from flask import jsonify, request
import pandas as pd
import json

def function():
    # Obtenemos los datos del cuerpo
    data = request.get_json()

    # Comprobamos que están todos los campos necesarios
    required_fields = [
        'year', 'brand', 'model', 'vehicle_class', 'engine_size', 'cylinders',
        'transmission', 'fuel_type', 'fuel_city_Lkm', 'fuel_hwy_Lkm', 'co2'
    ]

    # En caso de que falten datos, aparecerá un error
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f'Faltan campos: {", ".join(missing_fields)}'}), 400

    # Creamos una lista de diccionarios para pasárselo al pipeline
    input_data = pd.DataFrame([data])
    input_data['fuel_comb_Lkm'] = 0
    input_data['fuel_comb_mpg'] = 0

    # Cargamos el modelo
    import joblib
    modelo = joblib.load("model.joblib")

    # Predicción y devolvemos el resultado
    prediction = modelo.predict(input_data)
    result = prediction[0]
    
    return jsonify(f'Su vehículo consume {"%.2f" % result} mpg')