"""Deleting the table with the name ExampleTableTwo."""
import boto3
import pprint
import json

with open('./config/config.json', 'r') as file:
    config = json.loads(file.read())

dynamodb = boto3.resource(
    'dynamodb',
    region_name           = 'us-east-2',
    aws_access_key_id     = config['ID'],
    aws_secret_access_key = config['KEY']
)

table = dynamodb.Table('ExampleTableTwo')

response = table.delete()

printer = pprint.PrettyPrinter(indent=2)
printer.pprint(response)
