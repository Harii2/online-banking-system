from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.dtos import MakeTransactionDTO
from banking.exceptions.custom_exceptions import *


class MakeTransaction:
    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def make_transaction(self, make_transaction_dto: MakeTransactionDTO, presenter: PresenterImplementation):
        from_account_number = make_transaction_dto.from_account_number
        to_account_number = make_transaction_dto.to_account_number
        try:
            self.storage.validate_account_id(make_transaction_dto.from_account_number)
        except InvalidAccountId:
            presenter.raise_invalid_account_id()
            return

        try:
            self.storage.validate_account_id(make_transaction_dto.to_account_number)
        except InvalidAccountId:
            presenter.raise_invalid_account_id()
            return

        try:
            self.storage.validate_amount(make_transaction_dto.amount)
        except InvalidAmount:
            presenter.raise_invalid_amount()
            return

        try:
            account_id = from_account_number if make_transaction_dto.transaction_type == 'DEBIT' else to_account_number
            self.storage.validate_debit_user_balance(account_id, amount=make_transaction_dto.amount)
        except InsufficientBalance:
            presenter.raise_insufficient_balance()
            return

        make_transaction_response_dto = self.storage.make_transaction(make_transaction_dto)
        return presenter.get_make_transaction_response(make_transaction_response_dto)
