import json

def hello(event, context):
    #context.serverless_sdk.set_endpoint('/german/gutentag')
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

