FROM python:3.9-slim

RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev \
    && pip install --no-cache-dir boto3 pillow pytesseract

WORKDIR /app
COPY . .

CMD ["python", "main.py"]