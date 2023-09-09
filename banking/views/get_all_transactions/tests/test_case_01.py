"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {
            "account_id": "ibgroup"
        },
        "query_params": {
            "limit": 452,
            "offset": 46,
            "sortBy": 206,
            "type": "credit"
        },
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetAllTransactionsAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        self.default_test_case()  # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
