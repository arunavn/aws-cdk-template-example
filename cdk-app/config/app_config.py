"""
Config module to provide various config variable to other files
"""
import os
import json


class Config:
    """
    The config class to read the config json and proved values
    """
    def __init__(self) -> None:
        """constructor"""
        with open('config/app_config.json', 'r', encoding='utf-8') as f_p:
            self.config_dict = json.load(f_p)
        self.deploy_env = os.environ['DEPLOY_ENV']
        self.env_dict = self.config_dict.get(self.deploy_env, None)
        self.isdr = os.environ['REGION'] == self.env_dict['drRegion']

    def stack_name(self) -> str:
        """stack name"""
        return self.config_dict.get('stackName', '')

    def account_id(self) -> str:
        """account id"""
        return os.environ['ACCOUNT']

    def deploy_region(self) -> str:
        """deploy region"""
        return self.env_dict['primaryRegion']

    def primary_region(self) -> str:
        """primary region"""
        return self.env_dict['primaryRegion']

    def dr_region(self) -> str:
        """dr region"""
        return self.env_dict['drRegion']

    def generate_resource_name(self, resource_name) -> str:
        """generate resource name"""
        stack_prefix = self.config_dict['stackPrefix']
        region = self.deploy_region()
        return f"{stack_prefix}-{resource_name}-{self.deploy_env}-{region}"

    def generate_resource_id(self, resource_id) -> str:
        """generate resource id"""
        stack_prefix = self.config_dict['stackPrefix']
        region = self.deploy_region()
        region = region.replace('-', '')
        return f"{stack_prefix}{resource_id}{self.deploy_env}{region}"
