import os
import requests
from flask import jsonify

HOOK = "https://api.render.com/deploy/srv-cvrvcpeuk2gs73bm9sog?key=yr0QJ_krr-8"

def redeploy():
    if not HOOK:
        return jsonify({"error": "Redeploy hook no configurado"}), 500
    try:
        r = requests.post(HOOK, timeout=10)
    except requests.RequestException as e:
        return jsonify({"error": f"Error al conectar con el hook: {str(e)}"}), 500

    if r.status_code not in (200, 201, 202):
        return jsonify({"error": f"Hook falló: {r.text}"}), 500
    return jsonify({"detail": "Deploy solicitado correctamente"}), 202