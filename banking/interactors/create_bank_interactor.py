from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *
from .dtos import CreateBankRequestDTO


class CreateBankInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_bank(self, create_bank_request_dto: CreateBankRequestDTO,
                    presenter: PresenterImplementation):
        try:
            bank_id, manager_id = self.create_bank_wrapper(create_bank_request_dto=create_bank_request_dto)
        except IFSCCodeAlreadyExists:
            return presenter.raise_ifsc_code_already_exists()
        except ManagerEmailAlreadyExists:
            return presenter.raise_manager_email_already_exists()
        else:
            return presenter.get_create_bank_response(bank_id=bank_id, manager_id=manager_id)

    def create_bank_wrapper(self, create_bank_request_dto: CreateBankRequestDTO) -> tuple[int, int]:
        ifsc_code = create_bank_request_dto.ifsc_code
        bank_manager_email = create_bank_request_dto.bank_manager_email
        self.storage.validate_ifsc_code(ifsc_code=ifsc_code)
        self.storage.manager_already_exists(manager_email=bank_manager_email)
        bank_id = self.storage.create_bank(create_bank_request_dto=create_bank_request_dto)
        manager_id = self.storage.create_manager_for_bank(bank_id=bank_id, manager_email=bank_manager_email)
        return bank_id, manager_id
