import os

from sanic import Sanic
from sanic_cors import CORS

# Default configuration is development:
os.environ.setdefault(
    'SIMPLE_SETTINGS', 'server.config.development')
from simple_settings import settings

from server.api import api


# Core:
app = Sanic('elizabeth-cloud')
app.config.update(settings.as_dict())
app.blueprint(api)

# Plugins:
CORS(app=app, methods=['GET', 'HEAD', 'OPTION'], resources={
    r"/api/*": {
        "origins": "*",
    },
})


if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=int(settings.PORT),
        workers=settings.WORKERS
    )
