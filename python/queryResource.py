import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

with open('./config/config.json', 'r') as file:
    config = json.loads(file.read())

dynamodb = boto3.resource(
    'dynamodb',
    region_name           = 'us-east-2',
    aws_access_key_id     = config['ID'],
    aws_secret_access_key = config['KEY']
)

table = dynamodb.Table('ExampleTableTwo')

response = table.query(
    KeyConditionExpression=Key('id').eq(22)
)

for i in response['Items']:
    print(i)