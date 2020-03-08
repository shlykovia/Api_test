import pytest
from fixture.application import Application
from config  import api_config

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None or not fixture.api_healthcheck():
        fixture = Application(base_url=api_config["baseurl"])
    return fixture
