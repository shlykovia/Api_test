def test_get_user(app):
    if app.github_api.api_healthcheck():
        app.github_api.get_user()
