from sanic import Sanic

from sanic_cors import CORS

from server.api import api

from simple_settings import settings


# Core:
app = Sanic('elizabeth-cloud')
app.config.update(settings.as_dict())
app.blueprint(api)

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
