from sanic import Sanic

from app.config import configs


def create_app(config):
    """Create application instance.
    
    :param config: Config object.
    :return: Sanic application instance.
    """
    app = Sanic(__name__)
    app.config.from_object(config)

    # Register blueprints here:

    # ...
    # ...

    return app
