# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "create_account"
REQUEST_METHOD = "post"
URL_SUFFIX = "{bank_id}/account/create/v1/"


from .test_case_01 import TestCase01CreateAccountAPITestCase

__all__ = [
    "TestCase01CreateAccountAPITestCase"
]

