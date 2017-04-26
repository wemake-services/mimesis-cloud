"""
These settings are used for production and for production __only__.

These settings are used to deploy to Heroku.
It is required to modify them, if deploying to other infrastructure.
"""

import os

from ._common import *  # NOQA


PORT = os.environ.get('PORT', 8000)
HOST = os.environ.get('HOST', '0.0.0.0')
WORKERS = 4
