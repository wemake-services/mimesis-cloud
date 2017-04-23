class BaseConfig(object):
    APP_NAME = 'elizabeth-cloud'
    LOG_LEVEL = 'INFO'


class DevConfig(BaseConfig):
    HOST = ''
    PORT = ''
    WORKERS = ''
    LOG_LEVEL = 'DEBUG'


class TestConfig(DevConfig):
    pass


class ProdConfig(BaseConfig):
    pass


class HerokuConfig(ProdConfig):
    pass


configs = {
    'heroku': HerokuConfig,
    'test': TestConfig,
    'dev': DevConfig
}
