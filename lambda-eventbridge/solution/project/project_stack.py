from typing import cast
from aws_cdk import (
    Stack,
    aws_events as events,
    aws_events_targets as event_targets,
    aws_lambda as lambda_,
    aws_sqs as sqs,
)
from constructs import Construct

class ProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(self, "ProjectQueue")

        lambda_function = lambda_.Function(
            self, "LambdaPython",
            runtime=lambda_.Runtime.PYTHON_3_12,
            handler="hello_world.handler",
            code=lambda_.Code.from_asset("lambda"),
            environment= {
                "QUEUE_URL": queue.queue_url,
            }
        )

        rule = events.Rule(self, "rule",
            event_pattern=events.EventPattern(
                source=["awsworkshop.hello"]
            )
        )

        dlq = sqs.Queue(self, "DeadLetterQueue")

        rule.add_target(event_targets.LambdaFunction(
            cast(lambda_.IFunction, lambda_function),
            dead_letter_queue=dlq,
            retry_attempts=2
        ))

        queue.grant_send_messages(lambda_function)
