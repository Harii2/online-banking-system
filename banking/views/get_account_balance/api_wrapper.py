import json

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass

from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.get_account_balance_interactor import GetAccountBalanceInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']

    account_id = path_params['account_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetAccountBalanceInteractor(storage=storage)
    return interactor.get_accountant_balance_wrapper(account_id=account_id, presenter=presenter)
