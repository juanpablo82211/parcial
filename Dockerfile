FROM python:3.8-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libcurl4-openssl-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de dependencias y luego instalarlas
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copiar el código fuente al contenedor
COPY . /app
WORKDIR /app

# Exponer el puerto en el que Flask escuchará
EXPOSE 5000

# Ejecutar la aplicación Flask
CMD ["python", "app.py"]
