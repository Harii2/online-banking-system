from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *
from banking.interactors.dtos import *


class GetTransactionHistoryInteractor:
    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def get_transaction_history(self, account_id: int, query_params_dto: GetAllTransactionsQueryParamsDTO,
                                presenter: PresenterImplementation):
        try:
            self.storage.validate_account_id(account_id)
        except InvalidAccountId:
            presenter.raise_invalid_account_id()
            return
        transaction_history_response_dto = self.storage.get_transaction_history(account_id, query_params_dto)
        transaction_history = presenter.get_transaction_history_response(transaction_history_response_dto)
        return transaction_history
