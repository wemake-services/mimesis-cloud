import os
import sys

import pytest


root = os.path.dirname(os.path.dirname(__file__))
src = os.path.join(root, 'src')
sys.path.insert(0, src)


@pytest.fixture(scope='module')
def app():
    from app import app
    return app
