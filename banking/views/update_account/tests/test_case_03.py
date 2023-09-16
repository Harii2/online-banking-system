"""
# Updated Succesfully
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.models import Account
from banking.tests.factories.models import AccountFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "name": "Hari",
    "age": 21
}
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


class TestCase03UpdateAccountAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Arrange
        AccountFactory(id=1, name='Ram', age=20)

        # Assert
        self.default_test_case()
        account = Account.objects.get(id=1)
        assert account.name == 'Hari'
        assert account.age == 21
