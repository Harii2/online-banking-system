"""
# Created Account Succesfully
"""
import json

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.models import Account
from banking.tests.factories.models import BankFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "name": "Ramu",
    "age": 20,
    "mobile_number": "9998886660"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {
            "bank_id": "1234"
        },
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01CreateAccountAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Arrange
        BankFactory(id=1234)

        # Assert
        response = self.default_test_case()
        response_data = json.loads(response.content)
        account_number = response_data['account_number']
        account = Account.objects.get(id=account_number)
        account.name = 'Ramu'
        account.age = 20
        account.mobile_number = '9998886660'



