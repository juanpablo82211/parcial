import pytesseract
from PIL import Image
import io

def procesar_imagen(imagen_bytes):
    imagen = Image.open(io.BytesIO(imagen_bytes))
    texto = pytesseract.image_to_string(imagen)
    return extraer_datos_texto(texto)

def extraer_datos_texto(texto):
    lineas = texto.split("\n")
    datos = {
        "numero_recibo": None,
        "fecha": None,
        "total": None,
        "nombre_restaurante": None
    }
    for linea in lineas:
        if "Recibo" in linea:
            datos["numero_recibo"] = linea.split()[-1]
        elif "Fecha" in linea:
            datos["fecha"] = linea.split()[-1]
        elif "Total" in linea:
            datos["total"] = linea.split()[-1]
        elif "Restaurante" in linea:
            datos["nombre_restaurante"] = linea.replace("Restaurante", "").strip()
    return datos
