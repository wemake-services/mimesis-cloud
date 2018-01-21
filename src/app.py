from sanic import Sanic
from sanic_cors import CORS

from simple_settings import settings

from server.api import api
from server.graphql import view


# Core:
app = Sanic('mimesis-cloud')
app.config.update(settings.as_dict())
app.blueprint(api)
app.add_route(view, '/ql')

# Plugins:
CORS(app=app, methods=['GET', 'HEAD', 'OPTION'], resources={
    r'/api/*': {
        'origins': '*',
    },
})


if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=int(settings.PORT),
        workers=settings.WORKERS,
    )
