"""Stack declaration"""
from aws_cdk import (
    Stack
)
from constructs import Construct
# from config import app_config
from services import sqs_service


class CdkAppStack(Stack):
    """The stack class"""
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # app_config_obj = app_config.Config()
        sqs_service.create_basic_sqs(stack=self)
        sqs_service.create_standard_queue(stack=self)
