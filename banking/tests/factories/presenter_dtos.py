import factory
from banking.interactors.dtos import TransactionHistoryResponseDTO, TransactionDTO
import datetime


class TransactionDTOFactory(factory.Factory):
    class Meta:
        model = TransactionDTO

    transaction_id = factory.Sequence(lambda n: n)
    transaction_type = 'DEBIT'
    amount = 100
    date_time = factory.LazyFunction(datetime.datetime.now)
    account_id = 1


class TransactionHistoryResponseDTOFactory(factory.Factory):
    class Meta:
        model = TransactionHistoryResponseDTO

    transaction_history = factory.List([factory.SubFactory(TransactionDTOFactory) for _ in range(5)])
