from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from banking.storages.storage_implementation import StorageImplementation
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.interactors.account_make_transaction import AccountMakeTransaction
from banking.interactors.dtos import SelfTransactionRequestDTO


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs['path_params']
    request_body = kwargs['request_data']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AccountMakeTransaction(storage=storage)
    self_transaction_request_dto = SelfTransactionRequestDTO(
        account_number=request_body['account_number'],
        amount=request_body['amount'],
        transaction_type=request_body['transaction_type'].upper()
    )

    return interactor.account_make_transaction_wrapper(self_transaction_request_dto=self_transaction_request_dto,
                                               presenter=presenter)
