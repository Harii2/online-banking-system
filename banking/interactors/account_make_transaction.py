from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.dtos import SelfTransactionRequestDTO
from banking.exceptions.custom_exceptions import *


class AccountMakeTransaction:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def account_make_transaction_wrapper(self, self_transaction_request_dto: SelfTransactionRequestDTO,
                                         presenter: PresenterImplementation):
        try:
            make_transaction_response_dto = self.account_make_transaction(
                self_transaction_request_dto=self_transaction_request_dto)
        except InvalidAccountId:
            return presenter.raise_invalid_account_id()
        except InvalidAmount:
            return presenter.raise_invalid_amount()
        except InsufficientBalance:
            return presenter.raise_insufficient_balance()
        else:
            return presenter.get_make_transaction_response(make_transaction_response_dto=make_transaction_response_dto)

    def account_make_transaction(self, self_transaction_request_dto: SelfTransactionRequestDTO):
        account_number = self_transaction_request_dto.account_number
        amount = self_transaction_request_dto.amount
        transaction_type = self_transaction_request_dto.transaction_type
        self.storage.validate_account_id(account_id=account_number)
        self.storage.validate_amount(amount=amount)
        if transaction_type == 'DEBIT':
            self.storage.validate_debit_user_balance(account_id=account_number, amount=amount)
        return self.storage.account_make_transaction(self_transaction_request_dto=self_transaction_request_dto)
