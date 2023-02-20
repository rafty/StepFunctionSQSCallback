import os
import json
import boto3


stepfunction = boto3.client('stepfunctions')
STATE_MACHINE_ARN = os.getenv('STATE_MACHINE_ARN')

#
# Enter JSON, when Lambda test.
# - Success Flow
# {
#     "request": "CALLBACK",
#     "expectation": "SUCCESS"
# }
#
# - Error Flow
# {
#     "request": "CALLBACK",
#     "expectation": "ERROR"
# }
#


def lambda_handler(event, context):
    print('start test function')
    print(json.dumps(event))

    response = stepfunction.start_execution(
        stateMachineArn=STATE_MACHINE_ARN,
        input=json.dumps(event['body'])
    )

    print('stepfunction execute response')
    print(json.dumps(response))

    return
