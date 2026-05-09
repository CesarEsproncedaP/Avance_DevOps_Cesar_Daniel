import boto3
s3 = boto3.client('s3', region_name='us-east-1')
bucket = 'devops-proyfinal-cesaresp'
with open('/home/ubuntu/proyecto/logs/prueba.txt', 'w') as f:
    f.write('Archivo de prueba DevOps')
s3.upload_file('/home/ubuntu/proyecto/logs/prueba.txt', bucket, 'prueba.txt')
print(f"Archivo subido correctamente al bucket {bucket}")
