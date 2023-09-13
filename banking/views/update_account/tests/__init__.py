# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "update_account"
REQUEST_METHOD = "patch"
URL_SUFFIX = "account/{account_id}/v1/"


from .test_case_01 import TestCase01UpdateAccountAPITestCase

__all__ = [
    "TestCase01UpdateAccountAPITestCase"
]

