import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.create_bank_interactor import CreateBankInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_body = kwargs['request_data']
    bank_name = request_body['bank_name']
    ifsc_code = request_body['ifsc_code']
    bank_manager_email = request_body['bank_manager_email']
    # branch = request_body['branch']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateBankInteractor(storage)
    bank_id_dict = interactor.create_bank(
        bank_name=bank_name,
        ifsc_code=ifsc_code,
        bank_manager_email=bank_manager_email,
        branch="Hyderabad",
        presenter=presenter
    )
    response_data = json.dumps(bank_id_dict)
    return HttpResponse(response_data, status=201)
