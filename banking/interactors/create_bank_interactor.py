from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *


class CreateBankInteractor:

    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def create_bank(self, bank_name: str, ifsc_code: str, bank_manager_email: str, branch: str,
                    presenter: PresenterImplementation):
        try:
            self.storage.validate_ifsc_code(ifsc_code)
        except IFSCCodeAlreadyExists:
            presenter.raise_ifsc_code_already_exists()
            return

        try:
            self.storage.is_manager_already_exists(bank_manager_email)
        except ManagerEmailAlreadyExists:
            presenter.raise_manager_email_already_exists()
            return

        bank = self.storage.create_bank(bank_name, ifsc_code, bank_manager_email, branch)
        manager = self.storage.create_manager_for_bank(bank, bank_manager_email)
        manager_id = manager.id
        bank_id = bank.id
        return presenter.get_create_bank_response(bank_id, manager_id)
