from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
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

        topic = sns.Topic(
            self, "ProjectTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))

        lambda_function = lambda_.Function(
            self, "LambdaSqsSns",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="hello_world.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment={
                "TOPIC_ARN": topic.topic_arn,
            }
        )

        queue.grant_send_messages(lambda_function)
        topic.grant_publish(lambda_function)
        lambda_function.add_event_source(lambda_event_sources.SqsEventSource(queue))
