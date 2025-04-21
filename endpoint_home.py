def function():
    return """
    <h1>Team Challenge Bender</h1>

        <p>Bienvenid@ a nuestra API, aquí podrás interactuar con nuestro modelo y obtener predicciones sobre el consumo de tu vehículo.</p>

    <h2>Endpoints disponibles:</h2>
    <ul>
        <li><a href="/"><b>/</b></a>  → La página principal con las instrucciones (donde estás ahora ;) )</li>
        <li><a href="/api/v1/predict"><b>/api/v1/predict</b></a> → Devuelve una predicción. Necesitas pasarle parámetros.</li>
        <li><a href="/api/v1/retrain"><b>/api/v1/retrain</b></a> → Reentrena el modelo con nuevos datos.</li>
    </ul>

       <h3>Cómo usar el endpoint /api/v1/predict?  </h3>
            <p> Rellena estos parámetros en tu predicción:</p>
            <ul>
                <li>year</li>
                <li>brand</li>
                <li>model</li>
                <li>vehicle_class</li>
                <li>engine_size</li>
                <li>cylinders</li>
                <li>transmission</li>
                <li>fuel_type</li>
                <li>fuel_city_Lkm</li>
                <li>fuel_hwy_Lkm</li>
                <li>co2</li>
            </ul>
<p>Gracias por usar nuestra API ✌️</p>
 <img src="https://cdn.businessinsider.es/sites/navi.axelspringer.es/public/media/image/2022/02/futurama-regreso-2612065.jpg?tf=1200x" width="400" />

    """
