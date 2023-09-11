from abc import abstractmethod
from banking.models import Bank, Staff, Account
from banking.interactors.dtos import CreateBankRequestDTO
from banking.interactors.dtos import CreateAccountRequestDTO


class StorageInterface:
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
    def is_manager_already_exists(self, manager_email: str):
        pass

    @abstractmethod
    def create_bank(self, create_bank_request_dto: CreateBankRequestDTO) -> int:
        pass

    @abstractmethod
    def create_manager_for_bank(self, bank_id: int, manager_email: str) -> int:
        pass

    @abstractmethod
    def is_valid_bank_id(self, bank_id: int):
        pass

    @abstractmethod
    def validate_user_details(self, create_account_request_dto: CreateAccountRequestDTO):
        pass

    @abstractmethod
    def create_account(self, create_account_request_dto: CreateAccountRequestDTO) -> int :
        pass
