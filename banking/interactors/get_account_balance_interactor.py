from banking.exceptions.custom_exceptions import *
from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.presenters.presenter_implementation import PresenterImplementation


class GetAccountBalanceInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_accountant_balance_wrapper(self, account_id: int, presenter: PresenterImplementation):
        try:
            balance = self.get_accountant_balance(account_id=account_id)
        except InvalidAccountId:
            return presenter.raise_invalid_account_id()
        else:
            response = presenter.get_account_balance_response(balance=balance)
            return response

    def get_accountant_balance(self, account_id: int) -> int:
        self.storage.validate_account_id(account_id=account_id)
        balance = self.storage.get_accountant_balance(account_id=account_id)
        return balance
