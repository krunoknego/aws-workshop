from typing import cast
from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_lambda as lambda_,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_sqs as sqs,
)
from constructs import Construct

class ProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "ProjectQueue",
            visibility_timeout=Duration.seconds(300),
        )

        bucket = s3.Bucket(
            self, "ProjectBucket",
            removal_policy=RemovalPolicy.DESTROY,
        )

        lambda_function = lambda_.Function(
            self, "LambdaS3",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="hello_world.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "QUEUE_URL": queue.queue_url,
            }
        )

        queue.grant_send_messages(lambda_function)

        # The issue arises because jsii, the interoperability layer used by AWS
        # CDK to bridge TypeScript with other languages (like Python), sometimes lacks
        # full structural type compatibility across languages, causing Python’s static
        # type checker (e.g., Pyright) to see mismatches between expected interfaces and
        # actual implementations even though they work at runtime.
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            cast(s3.IBucketNotificationDestination, s3n.LambdaDestination(
                cast(lambda_.IFunction, lambda_function)
            )),
        )
