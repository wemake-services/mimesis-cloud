from app import create_app
from app.config import configs

if __name__ == '__main__':
    app = create_app(config=configs['heroku'])
    app.run(host="0.0.0.0")
