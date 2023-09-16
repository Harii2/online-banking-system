"""
# Invalid Age
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.tests.factories.models import BankFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "name": "Ramu",
    "age": 2,
    "mobile_number": "1234567890"
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


class TestCase02CreateAccountAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Arrange
        BankFactory(id=1234)

        # Assert
        self.default_test_case()

