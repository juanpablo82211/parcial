from flask import Flask, render_template, redirect, url_for
from s3_utils import listar_imagenes, descargar_imagen, guardar_json
from ocr_processor import procesar_imagen

app = Flask(__name__)

INPUT_BUCKET = "parcialjuankeeper"
OUTPUT_BUCKET = "parcialjuanjson"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar')
def procesar_recibos():
    claves = listar_imagenes(INPUT_BUCKET)
    for key in claves:
        print(f"Procesando {key}...")
        imagen_bytes = descargar_imagen(INPUT_BUCKET, key)
        datos = procesar_imagen(imagen_bytes)
        json_key = key.rsplit('.', 1)[0] + '.json'
        guardar_json(OUTPUT_BUCKET, json_key, datos)
        print(f"Datos guardados como {json_key} en {OUTPUT_BUCKET}")
    return redirect(url_for('index'))  # Redirige a la página principal después de ejecutar

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)