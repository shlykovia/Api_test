import pytest
from fixture.application import Application
from config import api_config

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application(base_url=api_config["baseurl"])
    return fixture
