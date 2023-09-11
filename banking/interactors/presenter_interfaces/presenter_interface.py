from abc import abstractmethod
from banking.interactors.dtos import CreateBankResponseDTO


class PresenterInterface:
    @abstractmethod
    def get_account_balance_response(self, balance: int) -> dict:
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
    def raise_invalid_user_details(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_create_account_response(self, account_number: int) -> dict:
        pass

    @abstractmethod
    def get_create_bank_response(self, bank_id: int, manager_id: int) -> CreateBankResponseDTO:
        pass
