import json
from django.http import HttpResponse

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.create_account_interactor import CreateAccountInteractor
from banking.interactors.dtos import CreateAccountRequestDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']
    request_body = kwargs['request_data']

    bank_id = path_params['bank_id']

    name = request_body['name']
    age = request_body['age']
    mobile_number = request_body['mobile_number']
    create_account_request_dto = CreateAccountRequestDTO(
        bank_id=bank_id,
        name=name,
        age=age,
        mobile_number=mobile_number
    )

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateAccountInteractor(storage=storage)

    response = interactor.create_account_wrapper(create_account_request_dto=create_account_request_dto,
                                                 presenter=presenter)
    return response
