"""Stack declaration"""
from aws_cdk import (
    Stack,
)
from constructs import Construct
# from config import app_config
from services import sqs_service, s3_service, iam_service


class CdkAppStack(Stack):
    """The stack class"""
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # app_config_obj = app_config.Config()
        _ = sqs_service.create_basic_sqs(stack=self)
        standard_queue = sqs_service.create_standard_queue(stack=self)
        producer_bucket = s3_service.create_producer_bucket(
                stack=self, dest_sqs=standard_queue
            )
        consume_policy = iam_service.create_sqs_policies(
                stack=self,
                queue=standard_queue,
                queue_label="standardqueue"
            )
        lambda_role = iam_service.create_lambda_role(stack=self)
        consume_policy.attach_to_role(lambda_role)
        # Granting queue permission to the role
        standard_queue.grant_purge(lambda_role)
        standard_queue.grant_consume_messages(lambda_role)
        # Granting s3 permissions to the role
        producer_bucket.grant_read_write(lambda_role)
        producer_bucket.grant_delete(lambda_role)
