# elizabeth-cloud


## Prerequirements

We are using `python-3.6.1` to run this app.


## Development

### virtualenv

We are using `virtualenv` for development.

### Installing requirements

We are using `pip-tools` to specify dependencies.

Firstly, install `pip-tools` into your `virtualenv`:

```bash
pip install pip-tools
```

To install (or renew) existing dependencies run:

```bash
pip-sync
```

### Adding new dependencies

To add new dependency you will need to:

1. Add it to the `requirements.in`
2. Run `pip-compile requirements.in`
3. Install new dependencies with `pip-sync`


## Running

This command will run `sanic` with default `development` settings:

```bash
python -m sanic app.app --host=127.0.0.1 --port=8000
```

Or you can just run the `app.py` file:

```bash
python app.py
```

### Settings

To specify other settings we are using `simple_settings` module.

### Workers

To specify different number of workers add that option: `--workers=NUMBER`
So, the production command will be:

```bash
SIMPLE_SETTINGS='server.config.production' python -m sanic app.app --host=127.0.0.1 --port=8000 --workers=4
```


## Testing

We are using `py.test` for testing. Just run `py.test` to run all the tests with coverage, linting, imports order and other features. See `pytest.ini` for the whole list of settings and plugins.

### CI/CD

We are using `travis` to run tests on `CI`. It also deploys your code to `heroku` production server on successful push to `master` branch. So be careful.
