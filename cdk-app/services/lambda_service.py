"""Creating lambda resources"""
from aws_cdk import (
    Stack,
    aws_lambda_event_sources
)
from aws_cdk.aws_iam import Role
from aws_cdk.aws_sqs import Queue
from aws_cdk import aws_lambda as lambda_
from config import app_config


def create_consumer_lambda(stack: Stack, lambda_role: Role, queue: Queue) -> lambda_.Function:
    """Creating lambda that runns on sqs message"""
    app_config_obj = app_config.Config()
    c_func = lambda_.Function(
        stack,
        app_config_obj.generate_resource_id("consumerLambda"),
        runtime=lambda_.Runtime.PYTHON_3_10,
        handler="main.lambda_handler",
        code=lambda_.Code.from_asset('../source/lambda/lambda_consumer'),
        function_name=app_config_obj.generate_resource_name(
                "consumerLambda"
            ),
        role=lambda_role,
    )
    e_source = aws_lambda_event_sources.SqsEventSource(queue)
    c_func.add_event_source(e_source)
    return c_func
