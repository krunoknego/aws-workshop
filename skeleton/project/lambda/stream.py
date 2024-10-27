import json
import os
import boto3

# Outside of the handler function so that warm starts can reuse the client
sqs_client = boto3.client('sqs')
queue_url = os.environ['QUEUE_URL']

def handler(event, _):
    for record in event['Records']:
        message = record['dynamodb']['NewImage']
        sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message)
        )
    return {
        'statusCode': 200,
        'body': json.dumps('Messages sent to SQS queue.')
    }
