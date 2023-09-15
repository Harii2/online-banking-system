"""
# Invalid Account id
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.models import Account
from banking.tests.factories.models import AccountFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {
            "account_id": "1"
        },
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetAccountBalanceAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Act
        AccountFactory(id=1, balance=1000)

        # Assert
        self.default_test_case()
        account = Account.objects.get(id=1)
        assert account.balance == 1000

