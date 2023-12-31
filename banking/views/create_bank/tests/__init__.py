# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "create_bank"
REQUEST_METHOD = "post"
URL_SUFFIX = "bank/v1/"


from .test_case_01 import TestCase01CreateBankAPITestCase
from .test_case_02 import TestCase02CreateBankAPITestCase
from .test_case_03 import TestCase03CreateBankAPITestCase

__all__ = [
    "TestCase01CreateBankAPITestCase",
    "TestCase02CreateBankAPITestCase",
    "TestCase03CreateBankAPITestCase"
]

