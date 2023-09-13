from banking.exceptions.custom_exceptions import *
from banking.interactors.dtos import CreateAccountRequestDTO
from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.presenters.presenter_implementation import PresenterImplementation


class CreateBankInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_account_wrapper(
            self, create_account_request_dto: CreateAccountRequestDTO,
            presenter: PresenterImplementation
    ):
        try:
            account_number = self.create_account(create_account_request_dto=create_account_request_dto)
        except BankNotExists:
            return presenter.raise_bank_not_exists()
        except InvalidAccountantName:
            return presenter.raise_invalid_user_name()
        except InvalidAge:
            return presenter.raise_invalid_age()
        except InvalidMobileNumber:
            return presenter.raise_invalid_mobile_number()
        else:
            return presenter.get_create_account_response(account_number=account_number)

    def create_account(self, create_account_request_dto: CreateAccountRequestDTO) -> int:
        bank_id = create_account_request_dto.bank_id
        self.storage.validate_bank_id(bank_id=bank_id)
        self.storage.validate_user_details(create_account_request_dto=create_account_request_dto)
        account_number = self.storage.create_account(create_account_request_dto=create_account_request_dto)
        return account_number
