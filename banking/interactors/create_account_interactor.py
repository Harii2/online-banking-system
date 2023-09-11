from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *
from banking.interactors.dtos import CreateAccountRequestDTO

class CreateBankInteractor:

    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def create_account(self, create_account_request_dto: CreateAccountRequestDTO, presenter: PresenterImplementation):
        bank_id = create_account_request_dto.bank_id
        try:
            self.storage.is_valid_bank_id(bank_id)
        except BankNotExists:
            presenter.raise_bank_not_exists()
            return

        try:
            self.storage.validate_user_details(create_account_request_dto)
        except InvalidAccountantName:
            presenter.raise_invalid_user_name()
            return
        except InvalidAge:
            presenter.raise_invalid_age()
        except InvalidMobileNumber:
            presenter.raise_invalid_mobile_number()
            return

        account_number = self.storage.create_account(create_account_request_dto)
        account_number_dict = presenter.get_create_account_response(account_number)
        return account_number_dict
