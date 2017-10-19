import boto3
import json

with open('./config/config.json', 'r') as file:
    data = json.loads(file.read())

client = boto3.client(
    'dynamodb',
    aws_access_key_id=data['ID'],
    aws_secret_access_key=data['KEY']
)

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'fact',
            'AttributeType': 'S'
        },
    ],
    TableName='ExampleTableTwo',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'fact',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 2
    }
)

print(response)