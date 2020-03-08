import pytest
from json import loads


@pytest.mark.parametrize('user,repo', [('shlykovia', 'Api_test')])
def test_get_user_repos(app, user, repo):
    api_status_code = app.github_api.get_api_status()
    assert api_status_code == 200, f'Something wrong with API(response code {api_status_code})'
    request = app.github_api.get_user_repos(github_user=user)
    assert repo == loads(request.text)[0].get('name'), 'repo not found'
