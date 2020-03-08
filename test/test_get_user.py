import pytest
from json import loads


@pytest.mark.parametrize('user', ['shlykovia', 'octocat'])
def test_get_user(app, user):
    api_status_code = app.github_api.get_api_status()
    assert api_status_code == 200, f'Something wrong with API(response code {api_status_code})'
    request = app.github_api.get_user(github_user=user)
    assert user == loads(request.text).get('login'), 'user not found'

