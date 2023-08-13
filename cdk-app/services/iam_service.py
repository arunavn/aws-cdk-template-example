"""Contains iam resources"""
from aws_cdk import (
    Stack,
)
from aws_cdk import aws_iam as iam
from config import app_config


def create_lambda_role(stack: Stack) -> iam.Role:
    """Creatin a iam role
    that will be assigned to lambda"""
    app_config_obj = app_config.Config()
    l_role = iam.Role(
        stack,
        app_config_obj.generate_resource_id("lambdaRole"),
        assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        role_name=app_config_obj.generate_resource_name(
                    "lambda_role"
                )
    )
    return l_role
