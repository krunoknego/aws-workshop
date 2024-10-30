from aws_cdk import (
    Stack,
    aws_lambda_go_alpha as lambda_go,
)
from constructs import Construct

class ProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_go.GoFunction(
            self, "LambdaGo",
            entry="cmd/hello",
        )
