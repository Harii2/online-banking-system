# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "get_all_transactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "account/{account_id}/transaction_history/v1/"


from .test_case_01 import TestCase01GetAllTransactionsAPITestCase

__all__ = [
    "TestCase01GetAllTransactionsAPITestCase"
]

