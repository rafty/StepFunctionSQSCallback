import json
import boto3


step_function = boto3.client('stepfunctions')


def lambda_handler(event, context):
    print('Lambda function invoked from SQS')
    print(json.dumps(event))

    token = event['token']

    # Todo: messageから判断して、error、successを返す
    result = True

    if result:
        output = json.dumps(
            {
                'result': 'SUCCESS',
                'reason': 'no error',
            }
        )
        step_function.send_task_success(
            taskToken=token,
            output=output
        )
        print('Success Callback called')
    else:
        output = json.dumps(
            {
                'result': 'ERROR',
                'reason': 'some error',
            }
        )
        step_function.send_task_failure(
            taskToken=token,
            output=output
        )
        print('Success Callback called')

    return
