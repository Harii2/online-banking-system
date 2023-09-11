from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *


class CreateBankInteractor:

    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def create_account(self, bank_id: int, name: str, age: int, mobile_number: str, presenter: PresenterImplementation):
        try:
            self.storage.is_valid_bank_id(bank_id)
        except BankNotExists:
            presenter.raise_bank_not_exists()
            return

        try:
            self.storage.validate_user_details(name, age, mobile_number)
        except InvalidUserDetails:
            presenter.raise_invalid_user_details()
            return

        account = self.storage.create_account(bank_id, name, age, mobile_number)
        account_number = account.id
        account_number_dict = presenter.get_create_account_response(account_number)
        return account_number_dict
