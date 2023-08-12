"""Create all sqs related objects here
"""
from aws_cdk import (
    Stack,
    Duration,
)
from aws_cdk.aws_kms import (
    IKey
)
from aws_cdk import aws_sqs as sqs
from config import app_config


def create_basic_sqs(stack: Stack):
    """create test queue"""
    app_config_obj = app_config.Config()
    queue = sqs.Queue(
            stack, app_config_obj.generate_resource_name("CdkAppQueue"),
            visibility_timeout=Duration.seconds(300),
        )
    return queue


def create_standard_queue(stack: Stack, kms_key: IKey | None = None):
    """Creating and standard Queue, with Customer Managed 
    KMS key / SSE-SQS encryption(Using L2 construct)"""
    app_config_obj = app_config.Config()
    std_queue = sqs.Queue(
            stack,
            app_config_obj.generate_resource_id("standardQueue"),
            data_key_reuse= Duration.seconds(600),
            delivery_delay= Duration.seconds(1),
            encryption= sqs.QueueEncryption.SQS_MANAGED,
            # encryption= sqs.QueueEncryption.KMS,
            # encryption_master_key= kms_key,
            max_message_size_bytes= 262144,
            queue_name= app_config_obj.generate_resource_name("standard-queue"),
            retention_period= Duration.days(7),
            visibility_timeout= Duration.minutes(2)
        )
    return std_queue



