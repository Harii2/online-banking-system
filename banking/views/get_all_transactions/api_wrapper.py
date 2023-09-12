from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
import json
from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.get_transaction_history_interactor import GetTransactionHistoryInteractor
from django.http import HttpResponse
from banking.interactors.dtos import GetAllTransactionsQueryParamsDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']
    query_params = kwargs['query_params']

    limit = query_params['limit']
    offset = query_params['offset']
    sort_by = query_params['sortBy']
    type = query_params['type'].upper()

    query_params_dto = GetAllTransactionsQueryParamsDTO(
        limit=limit,
        offset=offset,
        sort_by=sort_by,
        type=type
    )

    account_id = path_params['account_id']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetTransactionHistoryInteractor(storage=storage)
    return interactor.get_transaction_history(account_id=account_id, query_params_dto=query_params_dto, presenter=presenter)
