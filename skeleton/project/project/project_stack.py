from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
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

        lambda_stream = lambda_.Function(
            self, "LambdaDynamoDbStream",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="stream.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "QUEUE_URL": queue.queue_url,
            }
        )

        queue.grant_send_messages(lambda_stream)

        table = dynamodb.Table(
            self, "ProjectTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING,
            ),
            removal_policy=RemovalPolicy.DESTROY,
            stream=dynamodb.StreamViewType.NEW_IMAGE,
        )

        lambda_stream.add_event_source(
            lambda_event_sources.DynamoEventSource(
                table,
                starting_position=lambda_.StartingPosition.TRIM_HORIZON
            )
        )

        lambda_write = lambda_.Function(
            self, "LambdaDynamoDbWrite",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="write.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TABLE_NAME": table.table_name,
            }
        )

        table.grant_write_data(lambda_write)
