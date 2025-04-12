import boto3
import json

s3 = boto3.client('s3')

def listar_imagenes(bucket):
    response = s3.list_objects_v2(Bucket=bucket)
    return [item['Key'] for item in response.get('Contents', []) if item['Key'].lower().endswith(('.jpg', '.png'))]

def descargar_imagen(bucket, key):
    response = s3.get_object(Bucket=bucket, Key=key)
    return response['Body'].read()

def guardar_json(bucket, key, datos):
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(datos).encode('utf-8'),
        ContentType='application/json'
    )
