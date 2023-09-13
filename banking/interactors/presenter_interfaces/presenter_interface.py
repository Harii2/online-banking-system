from abc import abstractmethod
from banking.interactors.dtos import *
from django.http import HttpResponse


class PresenterInterface:
    @abstractmethod
    def get_delete_account_response(self, deleted: str):
        pass
    @abstractmethod
    def get_update_account_response(self, updated: bool):
        pass
    @abstractmethod
    def get_make_transaction_response(self, make_transaction_response_dto: MakeTransactionResponseDTO):
        pass

    @abstractmethod
    def raise_insufficient_balance(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_invalid_amount(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_transaction_history_response(self, transaction_history: TransactionHistoryResponseDTO):
        pass

    @abstractmethod
    def get_account_balance_response(self, balance: int):
        pass

    @abstractmethod
    def raise_invalid_user_name(self, *args, **kwargs):
        pass

    def raise_invalid_mobile_number(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_invalid_age(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_invalid_account_id(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_manager_email_already_exists(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_ifsc_code_already_exists(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_bank_not_exists(self, *args, **kwargs):
        pass


    @abstractmethod
    def get_create_account_response(self, account_number: int) -> dict:
        pass

    @abstractmethod
    def get_create_bank_response(self, bank_id: int, manager_id: int) -> CreateBankResponseDTO:
        pass
