import boto3
import json
import os

# Outside of the handler function so that warm starts can reuse the client
dynamodb = boto3.resource('dynamodb')

def handler(event, _):
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    table.put_item(
        Item={
            'id': '1',
            'content': event,
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Message written to DynamoDB.')
    }
