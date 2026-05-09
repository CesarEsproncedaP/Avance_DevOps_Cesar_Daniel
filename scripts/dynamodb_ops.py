import boto3
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('devops-proyfinal-cesar-tabla')
tabla.put_item(Item={'id': '1', 'nombre': 'Cesar', 'rol': 'DevOps'})
tabla.put_item(Item={'id': '2', 'nombre': 'Daniel', 'rol': 'DevOps'})
print("Registros insertados")
response = tabla.get_item(Key={'id': '1'})
print(f"Registro leído: {response['Item']}")
tabla.update_item(
    Key={'id': '1'},
    UpdateExpression='SET rol = :r',
    ExpressionAttributeValues={':r': 'DevOps Engineer'}
)
print("Registro modificado")
tabla.delete_item(Key={'id': '2'})
print("Registro eliminado")
