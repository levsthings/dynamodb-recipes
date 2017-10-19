"""Scan the count of table."""
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

with open('./config/config.json', 'r') as file:
    config = json.loads(file.read())

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource(
    'dynamodb',
    region_name           = 'us-east-2',
    aws_access_key_id     = config['ID'],
    aws_secret_access_key = config['KEY']
)

table = dynamodb.Table('ExampleTableTwo')

response = table.scan(
    ProjectionExpression='id'
)

print(json.dumps(response['ScannedCount'], cls=DecimalEncoder))
