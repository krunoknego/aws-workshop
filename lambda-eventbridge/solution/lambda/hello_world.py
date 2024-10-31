import json
import os
import boto3

# Outside of the handler function so that warm starts can reuse the client
sqs_client = boto3.client('sqs')
queue_url = os.environ['QUEUE_URL']

def handler(event, _):
    sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(event)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Messages sent to SQS queue.')
    }
