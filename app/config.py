import os


class BaseConfig(object):
    APP_NAME = os.environ.get('FALCON_APP_NAME', 'elizabeth-cloud')
    LOG_LEVEL = 'INFO'


class DevConfig(BaseConfig):
    ENV = 'DEV'
    LOG_LEVEL = 'DEBUG'


class TestConf(BaseConfig):
    ENV = 'TEST'


class ProdConfig(BaseConfig):
    ENV = 'PROD'


class HerokuConfig(ProdConfig):
    ENV = 'HEROKU'


configs = {
    'heroku': HerokuConfig,
    'dev': DevConfig
}
