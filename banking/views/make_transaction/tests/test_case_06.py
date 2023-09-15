"""
# Succesfully made transaction
"""

from django_swagger_utils.utils.test import CustomAPITestCase

from banking.models import Account, Transaction
from banking.tests.factories.models import AccountFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "from_account_number": 1,
    "to_account_number": 2,
    "amount": 1000,
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


class TestCase01MakeTransactionAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def test_case(self):
        # Arrange
        AccountFactory(id=1, balance=1000)
        AccountFactory(id=2, balance=1000)
        # Assert
        self.default_test_case()
        acc1 = Account.objects.get(id=1)
        acc2 = Account.objects.get(id=2)
        transaction = Transaction.objects.get(id=1)
        assert acc1.balance == 1000 - transaction.amount
        assert acc2.balance == 1000 + transaction.amount
        assert transaction.from_account_id == acc1
        assert transaction.to_account_id == acc2

