"""
# Manager Email already exists
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.tests.factories.models import StaffFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "bank_name": "SBI",
    "ifsc_code": "SBI00001",
    "bank_manager_email": "sbibankmanager01@gamil.com",
    "branch":"ALLAGADDA"
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


class TestCase02CreateBankAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Arrange
        StaffFactory(email="sbibankmanager01@gamil.com")
        # Act
        self.default_test_case()




