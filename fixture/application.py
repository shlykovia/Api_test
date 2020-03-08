from fixture.github_api import Github


class Application:

    def __init__(self, base_url):
        self.base_url = base_url
        self.github_api = Github(self)
