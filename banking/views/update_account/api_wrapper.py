from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.update_account_interactor import UpdateAccountInteractor
from banking.interactors.dtos import UpdateAccountRequestDTO

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']
    request_body = kwargs['request_data']

    account_id = path_params['account_id']

    name = request_body['name']
    age = request_body['age']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interator = UpdateAccountInteractor(storage=storage)

    update_account_dto = UpdateAccountRequestDTO(
        account_id=account_id,
        name=name,
        age=age
    )

    return interator.update_account_wrapper(update_account_dto=update_account_dto, presenter=presenter)
