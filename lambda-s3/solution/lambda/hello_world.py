import json
import os
import boto3

# Outside of the handler function so that warm starts can reuse the client
sqs_client = boto3.client('sqs')
queue_url = os.environ['QUEUE_URL']

def handler(event, _):
    for record in event['Records']:
        print(record)
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']

        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps({
                'bucket_name': bucket_name,
                'object_key': object_key
            })
        )
        print(f"Sent message to SQS queue: {response}")
    return {
        'statusCode': 200,
        'body': json.dumps('Messages published to SNS topic')
    }
