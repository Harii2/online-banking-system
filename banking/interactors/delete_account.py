from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.exceptions.custom_exceptions import *


class DeleteAccount:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def delete_account_wrapper(self, account_id: int, presenter: PresenterImplementation):
        try:
            deleted = self.delete_account(account_id=account_id)
        except InvalidAccountId:
            return presenter.raise_invalid_account_id()
        else:
            return presenter.get_delete_account_response(deleted=deleted)

    def delete_account(self, account_id):
        self.storage.validate_account_id(account_id=account_id)
        deleted = self.storage.delete_account(account_id=account_id)
        return deleted
