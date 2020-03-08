from factory.api import Api
from requests import get
from config import api_config


class Github(Api):

    def __init__(self, app):
        self.app = app
        self.config = api_config.get('github')
        self.base_url = self.config.get('base_url')
        self.username = self.config.get('username')
        self.password = self.config.get('password')
        super().__init__(self.base_url)

    def get(self, relative_url='', params=None):
        return get(self.base_url+relative_url, params)

    def get_user(self, github_user):
        github_user = self.username if not github_user else github_user
        self.get(relative_url=f'users/{github_user}')

    def api_healthcheck(self):
        if self.get().status_code == 200:
            return True
        return None
