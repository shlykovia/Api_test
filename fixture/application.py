from requests import get


class Application:

    def __init__(self, base_url):
        self.base_url = base_url

    def api_healthcheck(self):
        if get(self.base_url).status_code != 200:
            return None
        return True


