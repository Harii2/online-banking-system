from banking.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from banking.constants.exception_messages import *
from typing import Dict


class PresenterImplementation(PresenterInterface):
    def raise_ifsc_code_already_exists(self, *args, **kwargs):
        raise BadRequest(*INVALID_IFSC_CODE)

    def raise_manager_email_already_exists(self, *args, **kwargs):
        raise BadRequest(*INVALID_MANAGER_EMAIL)

    def raise_bank_not_exists(self, *args, **kwargs):
        raise NotFound(*BANK_NOT_EXISTS)

    def raise_invalid_user_details(self, *args, **kwargs):
        raise BadRequest(*INVALID_USER_DETAILS)

    def get_create_bank_response(self, bank_id: int, manager_id: int) -> Dict[str, int]:
        bank_manager_ids_dict = {'bank_id': bank_id, 'manager_id': manager_id}
        return bank_manager_ids_dict

    def get_create_account_response(self, account_number: int) -> Dict[str, int]:
        account_number_dict = {'account_number': account_number}
        return account_number_dict
