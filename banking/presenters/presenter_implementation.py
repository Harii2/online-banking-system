from banking.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from banking.constants.exception_messages import *
from typing import Dict


class PresenterImplementation(PresenterInterface):
    def raise_ifsc_code_already_exists(self, *args, **kwargs):
        raise BadRequest(*INVALID_IFSC_CODE)

    def raise_manager_email_already_exists(self, *args, **kwargs):
        raise BadRequest(*INVALID_MANAGER_EMAIL)

    def get_create_bank_response(self, bank_id: int, manager_id: int) -> Dict[str, int]:
        bank_manager_ids_dict = {'bank_id': bank_id, 'manager_id': manager_id}
        return bank_manager_ids_dict
