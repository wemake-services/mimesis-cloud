import os

from app import create_app


def init_app(env, **kwargs):
    if not env:
        env = os.environ.get('FALCON_ENV', 'dev')

    return create_app(env.upper(), **kwargs)
