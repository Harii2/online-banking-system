"""
# Succesfully created Bank
"""
import json

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.models import Bank, Staff
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


class TestCase03CreateBankAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Act
        response = self.default_test_case()

        # Assert
        response_data = json.loads(response.content)
        bank_id = response_data['bank_id']
        manager_id = response_data['manager_id']

        bank = Bank.objects.get(id=bank_id)
        manager = Staff.objects.get(id=manager_id)

        assert bank.name == 'SBI'
        assert bank.ifsc_code == "SBI00001"
        assert bank.branch == 'ALLAGADDA'
        assert manager.email == "sbibankmanager01@gamil.com"








