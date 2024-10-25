import json
import os
import boto3

# Outside of the handler function so that warm starts can reuse the client
sns_client = boto3.client('sns')
topic_arn = os.environ['TOPIC_ARN']

def handler(event, _):
    for record in event['Records']:
        print(record['body'])
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=record['body']
        )
        print(f"Published message to SNS topic: {response}")

    return {
        'statusCode': 200,
        'body': json.dumps('Messages published to SNS topic')
    }
