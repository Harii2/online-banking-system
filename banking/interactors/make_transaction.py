from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.dtos import MakeTransactionRequestDTO
from banking.exceptions.custom_exceptions import *


class MakeTransactionInteractor:
    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def make_transaction_wrapper(self, make_transaction_dto: MakeTransactionRequestDTO, presenter: PresenterImplementation):
        try:
            make_transaction_response_dto = self.make_transaction(make_transaction_dto=make_transaction_dto)
        except InvalidAccountId:
            return presenter.raise_invalid_account_id()
        except InvalidAmount:
            return presenter.raise_invalid_amount()
        except InsufficientBalance:
            return presenter.raise_insufficient_balance()
        else:
            return presenter.get_make_transaction_response(make_transaction_response_dto=make_transaction_response_dto)

    def make_transaction(self, make_transaction_dto: MakeTransactionRequestDTO):
        from_account_number = make_transaction_dto.from_account_number
        to_account_number = make_transaction_dto.to_account_number
        type = make_transaction_dto.transaction_type
        debit_account_id = from_account_number if type == 'DEBIT' else to_account_number
        amount = make_transaction_dto.amount
        self.storage.validate_account_id(account_id=from_account_number)
        self.storage.validate_account_id(account_id=to_account_number)
        self.storage.validate_amount(amount=amount)
        self.storage.validate_debit_user_balance(account_id=debit_account_id,
                                                 amount=amount)
        make_transaction_response_dto = self.storage.make_transaction(make_transaction_dto=make_transaction_dto)
        return make_transaction_response_dto
