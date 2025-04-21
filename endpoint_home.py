def function():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Team Challenge Bender - API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                background-color: #f9f9f9;
                color: #333;
            }
            h1 {
                color: #2c3e50;
            }
            h2, h3 {
                color: #444;
                margin-top: 30px;
                border-bottom: 1px solid #ddd;
                padding-bottom: 5px;
            }
            ul {
                line-height: 1.6;
                padding-left: 20px;
            }
            li {
                margin-bottom: 5px;
            }
            a {
                color: #007BFF;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .nested-ul {
                margin-top: 5px;
                margin-bottom: 10px;
            }
            pre {
                background-color: #f0f0f0;
                padding: 15px;
                border-radius: 6px;
                font-family: monospace;
                white-space: pre-wrap;
            }
            img {
                display: block;
                margin: 30px auto;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                max-width: 100%;
            }
            footer {
                text-align: center;
                margin-top: 40px;
                font-size: 0.9em;
                color: #777;
            }
        </style>
    </head>
    <body>

        <h1>🤖 Team Challenge Bender</h1>

        <p>Bienvenid@ a nuestra API. Aquí podrás interactuar con nuestro modelo de Machine Learning para obtener predicciones sobre el consumo de tu vehículo.</p>

        <h2>Endpoints disponibles</h2>
        <ul>
            <li><b>(GET) /</b> - La página principal con las instrucciones (donde estás ahora 😉)</li>
            <li><b>(POST) /api/v1/predict</b> - Devuelve una predicción. Necesitas pasarle parámetros.</li>
            <li><b>(POST) /api/v1/redeploy</b> - Redespliega el modelo.</li>
        </ul>

        <h3>📩 Cómo usar el endpoint <code>/api/v1/predict</code></h3>
        <p>Este es un ejemplo de los datos que puedes enviar al endpoint:</p>

        <pre>
{
    "year": 1994,
    "brand": "Toyota",
    "model": "Hilux",
    "vehicle_class": "SUV",
    "engine_size": 2,
    "cylinders": 4,
    "transmission": "A4",
    "fuel_type": "X",
    "fuel_city_Lkm": 8.4,
    "fuel_hwy_Lkm": 7.5,
    "co2": 150
}
        </pre>

        <h3>📋 Valores permitidos para algunas variables</h3>
        <p>Estas son las opciones que puedes enviar en algunas variables categóricas:</p>
        <ul>
            <li><b>transmission</b>:
                <ul class="nested-ul">
                    <li>A - Automática</li>
                    <li>AM - Manual automatizada</li>
                    <li>AS - Automática con cambio secuencial</li>
                    <li>AV - Transmisión variable continua</li>
                    <li>M - Manual</li>
                    <li>3-10 - Número de marchas (por ejemplo, "A6")</li>
                </ul>
            </li>
            <li><b>fuel_type</b>:
                <ul class="nested-ul">
                    <li>X - Gasolina normal</li>
                    <li>Z - Gasolina premium</li>
                    <li>D - Diésel</li>
                    <li>E - Etanol (E85)</li>
                    <li>N - Gas natural</li>
                </ul>
            </li>
        </ul>

        <img src="https://cdn.businessinsider.es/sites/navi.axelspringer.es/public/media/image/2022/02/futurama-regreso-2612065.jpg?tf=1200x" alt="Bender" />

        <footer>
            ✌️ Gracias por usar nuestra API - Team Challenge Bender
        </footer>

    </body>
    </html>
    """
