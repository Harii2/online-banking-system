"""
# Invalid to account id
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.tests.factories.models import AccountFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "from_account_number": 1,
    "to_account_number": 2,
    "amount": 1,
    "transaction_type": "debit"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase02MakeTransactionAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Arrange
        AccountFactory(id=1)
        # Assert
        self.default_test_case()
