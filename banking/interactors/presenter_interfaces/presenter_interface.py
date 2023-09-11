from abc import abstractmethod


class PresenterInterface:
    @abstractmethod
    def raise_manager_email_already_exists(self, *args, **kwargs):
        pass

    @abstractmethod
    def raise_ifsc_code_already_exists(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_create_bank_response(self, bank_id: int, manager_id: int) -> dict:
        pass
