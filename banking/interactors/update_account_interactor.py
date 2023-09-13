from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.dtos import UpdateAccountRequestDTO
from banking.exceptions.custom_exceptions import *


class UpdateAccountInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def update_account_wrapper(self, update_account_dto: UpdateAccountRequestDTO, presenter: PresenterImplementation):
        try:
            updated = self.update_account(update_account_dto=update_account_dto)
        except InvalidAccountId:
            return presenter.raise_invalid_account_id()
        except InvalidAccountantName:
            return presenter.raise_invalid_user_name()
        except InvalidAge:
            return presenter.raise_invalid_age()
        else:
            return presenter.get_update_account_response(updated=updated)

    def update_account(self, update_account_dto: UpdateAccountRequestDTO):
        account_id = update_account_dto.account_id
        name = update_account_dto.name
        age = update_account_dto.age
        self.storage.validate_account_id(account_id=account_id)
        self.storage.validate_user_name(name=name)
        self.storage.validate_user_age(age=age)
        updated = self.storage.update_account_details(update_account_dto=update_account_dto)
        return updated
