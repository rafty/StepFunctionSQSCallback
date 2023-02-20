import json


def lambda_handler(event, context):
    print('success process Lambda function invoked')
    print(json.dumps(event))
    return

