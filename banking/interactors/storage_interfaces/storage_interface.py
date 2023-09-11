from abc import abstractmethod
from dataclasses import dataclass
from banking.models import Bank, Staff, Account


class StorageInterface:

    @abstractmethod
    def validate_ifsc_code(self, ifsc_code: str):
        pass

    @abstractmethod
    def is_manager_already_exists(self, manager_email: str):
        pass

    @abstractmethod
    def create_bank(self, bank_name: str, ifsc_code: str, bank_manager_email: str, branch: str):
        pass

    @abstractmethod
    def create_manager_for_bank(self, bank_id: int, manager_email: str) -> Staff:
        pass

    @abstractmethod
    def is_valid_bank_id(self, bank_id: int):
        pass

    @abstractmethod
    def validate_user_details(self, name: str, age: int, mobile_number: str):
        pass

    @abstractmethod
    def create_account(self, bank_id: int, name: str, age: int, mobile_number: str) -> Account:
        pass
