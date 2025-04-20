import joblib
from flask import jsonify, request

def function():
    # Cargamos el modelo
    modelo = joblib.load("model.joblib")

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
    input_data = [data]  

    # Predicción y devolvemos el resultado
    prediction = modelo.predict(input_data)
    
    return jsonify({'prediction': prediction[0]})