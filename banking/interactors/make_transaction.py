from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.dtos import MakeTransactionDTO
from banking.exceptions.custom_exceptions import InvalidAccountId

class MakeTransaction:
    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def make_transaction(self, make_transaction_dto: MakeTransactionDTO, presenter: PresenterImplementation) -> None:
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

        response = self.storage.make_transaction(make_transaction_dto)
        return presenter.make_transaction(response)
