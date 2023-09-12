from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
import json
from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.make_transaction import MakeTransaction
from banking.interactors.dtos import MakeTransactionDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']
    request_body = kwargs['request_data']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = MakeTransaction(storage=storage)
    make_transaction_dto = MakeTransactionDTO(
        from_account_number=request_body['from_account_number'],
        to_account_number=request_body['to_account_number'],
        amount=request_body['amount'],
        transaction_type=request_body['transaction_type'].upper()
    )
    return interactor.make_transaction(make_transaction_dto=make_transaction_dto, presenter=presenter)
