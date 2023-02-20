import json


def lambda_handler(event, context):
    print('error process Lambda function invoked')
    print(json.dumps(event))
    return
