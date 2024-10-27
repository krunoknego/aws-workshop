import json

def handler(event, _):
    print(event)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello World from Lambda')
    }
