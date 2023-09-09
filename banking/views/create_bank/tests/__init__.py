# pylint: disable=wrong-import-position

APP_NAME = "banking"
URL_BASE_PATH = "/api/"
OPERATION_NAME = "create_bank"
REQUEST_METHOD = "post"
URL_SUFFIX = "bank/"


from .test_case_01 import TestCase01CreateBankAPITestCase

__all__ = [
    "TestCase01CreateBankAPITestCase"
]

