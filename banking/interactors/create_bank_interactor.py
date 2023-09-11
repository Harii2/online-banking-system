from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *
from .dtos import CreateBankRequestDTO

class CreateBankInteractor:

    def __init__(self, storage: StorageImplementation):
        self.storage = storage

    def create_bank(self, create_bank_request_dto: CreateBankRequestDTO,
                    presenter: PresenterImplementation):
        ifsc_code = create_bank_request_dto.ifsc_code
        bank_manager_email = create_bank_request_dto.bank_manager_email
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

        bank_id = self.storage.create_bank(create_bank_request_dto)
        manager_id = self.storage.create_manager_for_bank(bank_id, bank_manager_email)
        return presenter.get_create_bank_response(bank_id, manager_id)

