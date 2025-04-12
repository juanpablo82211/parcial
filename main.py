from s3_utils import listar_imagenes, descargar_imagen, guardar_json
from ocr_processor import procesar_imagen

INPUT_BUCKET = "parcialjuankeeper"
OUTPUT_BUCKET = "parcialjuanjson"

def main():
    claves = listar_imagenes(INPUT_BUCKET)
    for key in claves:
        print(f"Procesando {key}...")
        imagen_bytes = descargar_imagen(INPUT_BUCKET, key)
        datos = procesar_imagen(imagen_bytes)
        json_key = key.rsplit('.', 1)[0] + '.json'
        guardar_json(OUTPUT_BUCKET, json_key, datos)
        print(f"Datos guardados como {json_key} en {OUTPUT_BUCKET}")

if __name__ == "__main__":
    main()