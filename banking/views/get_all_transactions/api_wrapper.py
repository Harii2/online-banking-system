from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
import json
from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.get_transaction_history_interactor import GetTransactionHistoryInteractor
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']
    account_id = path_params['account_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetTransactionHistoryInteractor(storage)
    return interactor.get_transaction_history(account_id, presenter)
