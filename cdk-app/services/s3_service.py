"""Contains s3 related objects"""
from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_s3_notifications as s3n
)
from aws_cdk.aws_kms import IKey
from aws_cdk.aws_sqs import Queue
from aws_cdk import aws_s3 as s3
from config import app_config


def create_producer_bucket(
            stack: Stack,
            dest_sqs: Queue | None = None,
            kms_key: IKey | None = None
        ) -> s3.Bucket:
    """Creating a bucket which send
    message to sqs when and object is created
    """
    app_config_obj = app_config.Config()
    p_bucket = s3.Bucket(
        stack,
        app_config_obj.generate_resource_id("producerBucket"),
        encryption=s3.BucketEncryption.S3_MANAGED,
        bucket_name=app_config_obj.generate_resource_name(
                    "producer-bucket"
                ),
        removal_policy=RemovalPolicy.RETAIN

    )
    if kms_key is not None:
        kms_key = None
    if dest_sqs is not None:
        p_bucket.add_event_notification(
                s3.EventType.OBJECT_CREATED,
                s3n.SqsDestination(dest_sqs),
                s3.NotificationKeyFilter(
                        prefix="upload/*",
                        suffix="*.txt",
                    ),
            )
    return p_bucket
