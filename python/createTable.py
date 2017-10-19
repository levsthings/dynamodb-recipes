import boto3
import json

with open('./config/config.json', 'r') as file:
    config = json.loads(file.read())

dynamodb = boto3.resource(
    'dynamodb',
    region_name           = 'us-east-2',
    aws_access_key_id     = config['ID'],
    aws_secret_access_key = config['KEY']
)

response = dynamodb.create_table(
    AttributeDefinitions = [
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'fact',
            'AttributeType': 'S'
        },
    ],
    TableName = 'ExampleTableTwo',
    KeySchema = [
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'fact',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

print(response.table_status)