import boto3
import json
from datetime import datetime

ec2 = boto3.client('ec2', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')

# a)
def crear_instancia():
    print("\n=== CREANDO INSTANCIA EC2 ===")
    response = ec2.run_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'devops-boto3'}]
        }]
    )
    instancia_id = response['Instances'][0]['InstanceId']
    print(f"Instancia creada: {instancia_id}")
    return instancia_id

# b)
def listar_instancias():
    print("\n=== INSTANCIAS EC2 ===")
    response = ec2.describe_instances()
    for reserva in response['Reservations']:
        for instancia in reserva['Instances']:
            print(f"ID: {instancia['InstanceId']} | Tipo: {instancia['InstanceType']} | Estado: {instancia['State']['Name']}")

# c)
def listar_buckets():
    print("\n=== BUCKETS S3 ===")
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"Bucket: {bucket['Name']}")
        try:
            objetos = s3.list_objects_v2(Bucket=bucket['Name'])
            if 'Contents' in objetos:
                for obj in objetos['Contents']:
                    print(f"  - {obj['Key']} ({obj['Size']} bytes)")
        except:
            print("  (sin acceso a objetos)")

# d)
def generar_reporte():
    print("\n=== REPORTE DE RECURSOS ===")
    reporte = {
        "fecha": str(datetime.now()),
        "instancias": [],
        "buckets": []
    }
    response = ec2.describe_instances()
    for reserva in response['Reservations']:
        for inst in reserva['Instances']:
            reporte["instancias"].append({
                "id": inst['InstanceId'],
                "tipo": inst['InstanceType'],
                "estado": inst['State']['Name']
            })
    response_s3 = s3.list_buckets()
    for bucket in response_s3['Buckets']:
        reporte["buckets"].append(bucket['Name'])

    with open('/home/ubuntu/proyecto/logs/reporte.json', 'w') as f:
        json.dump(reporte, f, indent=4)
    print(json.dumps(reporte, indent=4))
    print("\nReporte guardado en /home/ubuntu/proyecto/logs/reporte.json")

# Ejecutar funciones
listar_instancias()
listar_buckets()
generar_reporte()
