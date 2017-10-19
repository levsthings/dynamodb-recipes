import boto3
import pprint
import time
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

with open('./exampleData/data.json', 'r') as file:
    data = json.loads(file.read())

dataArray = data['data']

for i in dataArray:
    dataID   = i['id']
    dataFact = i['fact']
    response = table.put_item(
        Item= {
            'id'  : dataID,
            'fact': dataFact
        })
    printer = pprint.PrettyPrinter(indent=2)
    printer.pprint(response)
    time.sleep(.500)

