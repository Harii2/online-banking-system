from abc import abstractmethod
from banking.models import Bank, Staff, Account
from banking.interactors.dtos import CreateBankRequestDTO, CreateAccountRequestDTO, TransactionHistoryResponseDTO
from banking.interactors.dtos import *


class StorageInterface:
    @abstractmethod
    def delete_account(self, account_id: int):
        pass
    @abstractmethod
    def update_account_details(self, update_account_dto: UpdateAccountRequestDTO):
        pass
    @abstractmethod
    def account_make_transaction(self, self_transaction_request_dto: SelfTransactionRequestDTO) :
        pass
    @abstractmethod
    def validate_debit_user_balance(self, account_id: int, amount: int):
        pass

    @abstractmethod
    def make_transaction(self, make_transaction_dto: MakeTransactionDTO) -> MakeTransactionResponseDTO:
        pass

    @abstractmethod
    def validate_amount(self, amount: int):
        pass

    @abstractmethod
    def get_transaction_history(self, account_id: int,
                                query_params_dto: GetAllTransactionsQueryParamsDTO) -> TransactionHistoryResponseDTO:
        pass

    @abstractmethod
    def get_accountant_balance(self, account_id: int):
        pass

    @abstractmethod
    def validate_account_id(self, account_id: int):
        pass

    @abstractmethod
    def validate_ifsc_code(self, ifsc_code: str):
        pass

    @abstractmethod
    def manager_already_exists(self, manager_email: str):
        pass

    @abstractmethod
    def create_bank(self, create_bank_request_dto: CreateBankRequestDTO) -> int:
        pass

    @abstractmethod
    def create_manager_for_bank(self, bank_id: int, manager_email: str) -> int:
        pass

    @abstractmethod
    def validate_bank_id(self, bank_id: int):
        pass

    @abstractmethod
    def validate_user_details(self, create_account_request_dto: CreateAccountRequestDTO):
        pass

    @abstractmethod
    def validate_user_name(self, name: str):
        pass

    @abstractmethod
    def validate_user_age(self, age: int):
        pass

    @abstractmethod
    def validate_user_mobile_number(self, mobile_number: str):
        pass

    @abstractmethod
    def create_account(self, create_account_request_dto: CreateAccountRequestDTO) -> int:
        pass
