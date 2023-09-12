# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "make_transaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "bank/make_transaction/v1/"


from .test_case_01 import TestCase01MakeTransactionAPITestCase

__all__ = [
    "TestCase01MakeTransactionAPITestCase"
]

