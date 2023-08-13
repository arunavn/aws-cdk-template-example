"""Stack declaration"""
from aws_cdk import (
    Stack,
)
from constructs import Construct
# from config import app_config
from services import sqs_service, s3_service, iam_service
from services import lambda_service


class CdkAppStack(Stack):
    """The stack class"""
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # app_config_obj = app_config.Config()
        _ = sqs_service.create_basic_sqs(stack=self)
        # Queue
        standard_queue = sqs_service.create_standard_queue(stack=self)
        sqs_consume_policy, sqs_purge_policy, _ = iam_service.create_sqs_policies(
                stack=self,
                queue=standard_queue,
                queue_label="standardqueue"
            )
        # Bucket
        producer_bucket = s3_service.create_producer_bucket(
                stack=self, dest_sqs=standard_queue
            )
        # Role
        lambda_role = iam_service.create_lambda_role(stack=self)
        # Granting queue permission to the role
        sqs_consume_policy.attach_to_role(lambda_role)
        sqs_purge_policy.attach_to_role(lambda_role)
        # Granting s3 permissions to the role
        producer_bucket.grant_read_write(lambda_role)
        producer_bucket.grant_delete(lambda_role)
        _ = lambda_service.create_consumer_lambda(self, lambda_role)
