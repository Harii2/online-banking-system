from banking.exceptions.custom_exceptions import *

from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation


class GetAccountBalanceInteractor:

    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def get_accountant_balance(self, account_id: int, presenter: PresenterImplementation):
        try:
            self.storage.validate_account_id(account_id)
        except InvalidAccountId:
            presenter.raise_invalid_account_id()
            return
        balance = self.storage.get_accountant_balance(account_id)
        print(balance)
        balance_dict = presenter.get_account_balance_response(balance)
        return balance_dict
