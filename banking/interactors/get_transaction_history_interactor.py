from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *
from banking.interactors.dtos import *


class GetTransactionHistoryInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_transaction_history(self, account_id: int, query_params_dto: GetAllTransactionsQueryParamsDTO,
                                presenter: PresenterImplementation):
        try:
            transaction_history_response_dto = self.get_transaction_history_wrapper(account_id=account_id, query_params_dto=query_params_dto)
        except InvalidAccountId:
            presenter.raise_invalid_account_id()
            return
        else:
            transaction_history = presenter.get_transaction_history_response(transaction_history_response_dto=transaction_history_response_dto)
            return transaction_history

    def get_transaction_history_wrapper(self, account_id: int, query_params_dto: GetAllTransactionsQueryParamsDTO) -> TransactionHistoryResponseDTO:
        self.storage.validate_account_id(account_id=account_id)
        transaction_history_response_dto = self.storage.get_transaction_history(account_id=account_id, query_params_dto=query_params_dto)
        return transaction_history_response_dto
