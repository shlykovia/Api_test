from factory.api import Api
from requests import get


class Github(Api):

    def __init__(self, app):
        self.app = app
        super().__init__(app.base_url)

    def get(self, relative_url=None, params=None):
        return get(self.base_url+relative_url, params)

    def api_healthcheck(self):
        if get(self.base_url).status_code != 200:
            return None
        return True
