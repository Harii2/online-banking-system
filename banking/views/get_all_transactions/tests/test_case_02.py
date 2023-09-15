"""
# Retriveing all transaction for a debit type
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.models import Account, Transaction
from banking.tests.factories.models import TransactionFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {
            "account_id": "1"
        },
        "query_params": {
            "limit": 10,
            "offset": 0,
            "sort_by": "ASC",
            "type": "debit"
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
        # Act
        TransactionFactory()

        # Assert
        self.default_test_case()
        transaction = Transaction.objects.get(id=1)
        acc1 = Account.objects.get(id=1)
        acc2 = Account.objects.get(id=2)
        assert transaction.from_account_id_id == acc1.id
        assert transaction.to_account_id_id == acc2.id

