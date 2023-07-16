"""Entry point for the cdk app"""
# !/usr/bin/env python3
import aws_cdk as cdk
from cdk_app.cdk_app_stack import CdkAppStack
from config import app_config


app = cdk.App()
app_config_obj = app_config.Config()
CdkAppStack(
            app, app_config_obj.stack_name(),
            env=cdk.Environment(
                        account=app_config_obj.account_id(),
                        region=app_config_obj.deploy_region()
                        )
        )

app.synth()
