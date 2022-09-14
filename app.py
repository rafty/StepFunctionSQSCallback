#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.stepfunction_sqs_callback_stack import StepFunctionSqsCallbackStack

env = cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]),
)

app = cdk.App()
StepFunctionSqsCallbackStack(app, "StepFunctionSqsCallbackStack", env=env)

app.synth()
