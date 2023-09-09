import os


from online_banking_system.settings.base import *
from online_banking_system.settings.base_pg_db import *
from online_banking_system.settings.base_swagger_utils import *
from online_banking_system.settings.base_aws_s3 import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOG_DSU_OLD_VERSION_LOGS = False