import json
import os
import boto3

sqs_client = boto3.client('sqs')

def handler(event, context):
    print("Event: ", json.dumps(event))

    queue_url = os.environ['QUEUE_URL']

    for record in event['Records']:
        message_body = record['body']
        print(f"Processing message: {message_body}")

        # Send message to the SQS queue
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )

        print(f"Sent message to SQS: {response['MessageId']}")
