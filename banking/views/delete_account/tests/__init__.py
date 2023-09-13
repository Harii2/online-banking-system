# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "delete_account"
REQUEST_METHOD = "delete"
URL_SUFFIX = "account/{account_id}/v1/"


from .test_case_01 import TestCase01DeleteAccountAPITestCase

__all__ = [
    "TestCase01DeleteAccountAPITestCase"
]

