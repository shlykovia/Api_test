def test_get_user(app):
    if app.github_api.api_healthcheck():
        app.github_api.get(relative_url=f'/users/{app.github_api.username}')
