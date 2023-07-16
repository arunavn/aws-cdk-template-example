"""Create all sqs related objects here
"""
from aws_cdk import (
    Duration,
    aws_sqs as sqs,
)
from config import app_config


def create_test_sqs(stack):
    """create test queue"""
    app_config_obj = app_config.Config()
    queue = sqs.Queue(
            stack, app_config_obj.generate_resource_name("CdkAppQueue"),
            visibility_timeout=Duration.seconds(300),
        )
    return queue
