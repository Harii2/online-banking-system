import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.create_bank_interactor import CreateBankInteractor
from banking.interactors.dtos import CreateBankRequestDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_body = kwargs['request_data']
    bank_name = request_body['bank_name']
    ifsc_code = request_body['ifsc_code']
    branch = request_body['branch']
    bank_manager_email = request_body['bank_manager_email']
    # branch = request_body['branch']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateBankInteractor(storage)
    create_bank_request_dto = CreateBankRequestDTO(
        bank_name=bank_name,
        ifsc_code=ifsc_code,
        bank_manager_email=bank_manager_email,
        branch=branch
    )
    create_bank_response_dto = interactor.create_bank(
        create_bank_request_dto,
        presenter=presenter
    )
    bank_manager_ids_dict = {
        "manager_id": create_bank_response_dto.manager_id,
        "bank_id": create_bank_response_dto.bank_id
    }
    response_data = json.dumps(bank_manager_ids_dict)
    return HttpResponse(response_data, status=201)
