# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "get_account_balance"
REQUEST_METHOD = "get"
URL_SUFFIX = "account/{account_id}/v1/"


from .test_case_01 import TestCase01GetAccountBalanceAPITestCase

__all__ = [
    "TestCase01GetAccountBalanceAPITestCase"
]

