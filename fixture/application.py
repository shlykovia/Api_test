from fixture.github_api import Github


class Application:

    def __init__(self):
        self.github_api = Github(self)
