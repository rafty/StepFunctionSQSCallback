from aws_cdk import Stack
from constructs import Construct
from constructors.stepfunctions import StepFunctionsCallbackPattern


class StepFunctionSqsCallbackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        StepFunctionsCallbackPattern(self, 'StepFunctionsCallbackPatternConstructor')
