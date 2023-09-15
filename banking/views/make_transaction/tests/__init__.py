# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "make_transaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "bank/make_transaction/v1/"


from .test_case_01 import TestCase01MakeTransactionAPITestCase
from .test_case_02 import TestCase02MakeTransactionAPITestCase
from .test_case_03 import TestCase03MakeTransactionAPITestCase
from .test_case_04 import TestCase04MakeTransactionAPITestCase
from .test_case_05 import TestCase05MakeTransactionAPITestCase
from .test_case_06 import TestCase06MakeTransactionAPITestCase

__all__ = [
    "TestCase01MakeTransactionAPITestCase",
    "TestCase02MakeTransactionAPITestCase",
    "TestCase03MakeTransactionAPITestCase",
    "TestCase04MakeTransactionAPITestCase",
    "TestCase05MakeTransactionAPITestCase",
    "TestCase06MakeTransactionAPITestCase"
]

