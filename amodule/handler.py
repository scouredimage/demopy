import json
import secrets

def hello(event, context):
    #context.serverless_sdk.set_endpoint('/german/gutentag')
    lucky = secrets.choice(range(100))
    body = {
        "message": f"Hello! Your lucky number is {lucky}",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

