import uuid

from online_banking_system.settings.local import *
from online_banking_system.settings.base_pg_db import *

DATABASES['default']['TEST'].update({
    'NAME':  str(uuid.uuid4()),
    'ENGINE': os.environ.get('RDS_DB_ENGINE'),
    'CHARSET': 'UTF8'
})

