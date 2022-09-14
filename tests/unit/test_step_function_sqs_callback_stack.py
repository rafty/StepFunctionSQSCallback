import aws_cdk as core
import aws_cdk.assertions as assertions

from stacks.step_function_sqs_callback_stack import StepFunctionSqsCallbackStack

# example tests. To run these tests, uncomment this file along with the example
# resource in step_function_sqs_callback/step_function_sqs_callback_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StepFunctionSqsCallbackStack(app, "step-function-sqs-callback")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
