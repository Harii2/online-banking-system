# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "account_make_transaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "account/make_transaction/v1/"


from .test_case_01 import TestCase01AccountMakeTransactionAPITestCase
from .test_case_02 import TestCase02AccountMakeTransactionAPITestCase
from .test_case_03 import TestCase03AccountMakeTransactionAPITestCase
from .test_case_04 import TestCase04AccountMakeTransactionAPITestCase
from .test_case_05 import TestCase05AccountMakeTransactionAPITestCase

__all__ = [
    "TestCase01AccountMakeTransactionAPITestCase",
    "TestCase02AccountMakeTransactionAPITestCase",
    "TestCase03AccountMakeTransactionAPITestCase",
    "TestCase04AccountMakeTransactionAPITestCase",
    "TestCase05AccountMakeTransactionAPITestCase"
]

