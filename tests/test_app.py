import pytest

from sanic.exceptions import NotFound
from sanic.response import text


@pytest.fixture(scope='module')
def app():
    from server.app import app
    return app


def test_resource_is_ok(app):
    _, response = app.test_client.get('/api/food/dish')
    assert response.status == 200


def test_bad_resource(app):
    _, response = app.test_client.get('/not_found_404')
    assert response.status == 404


def test_bad_sub_name(app):
    _, response = app.test_client.get('/api/food/badsubmane')
    assert response.status == 404


def test_catch_not_found_404(app):
    @app.exception([NotFound])
    def exception_list(request, exception):
        return text('not_found')

    _, response = app.test_client.get('/not_found_404')
    assert response.text == 'not_found'

    _, response = app.test_client.get('/api/food/dich')
    assert response.text == 'not_found'
