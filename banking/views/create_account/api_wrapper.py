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
    path_params = kwargs['path_params']
    request_body = kwargs['request_data']

    bank_id = path_params['bank_id']

    name = request_body['name']
    age = request_body['age']
    mobile_number = request_body['mobile_number']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateBankInteractor(storage)

    account_number_dict = interactor.create_account(bank_id, name, age, mobile_number, presenter)
    response_dict = json.dumps(account_number_dict)
    return HttpResponse(response_dict, status=201)

