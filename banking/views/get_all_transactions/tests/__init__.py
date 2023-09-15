# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "get_all_transactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "account/{account_id}/transaction_history/v1/"


from .test_case_01 import TestCase01GetAllTransactionsAPITestCase
from .test_case_02 import TestCase02GetAllTransactionsAPITestCase
from .test_case_03 import TestCase03GetAllTransactionsAPITestCase

__all__ = [
    "TestCase01GetAllTransactionsAPITestCase",
    "TestCase02GetAllTransactionsAPITestCase",
    "TestCase03GetAllTransactionsAPITestCase"
]

