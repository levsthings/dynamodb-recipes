import boto3
import pprint
import json

with open('./config/config.json', 'r') as file:
    data = json.loads(file.read())

client = boto3.client(
    'dynamodb',
    aws_access_key_id=data['ID'],
    aws_secret_access_key=data['KEY']
)

response = client.delete_table(
    TableName='ExampleTableTwo'
)

printer = pprint.PrettyPrinter(indent=2)
printer.pprint(response)
