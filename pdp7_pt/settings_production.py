import os

import dj_database_url

from pdp7_pt.settings import *


DEBUG = False
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = os.urandom(100).decode('ascii', errors='ignore')
ALLOWED_HOSTS = ['*']
