import factory
from banking.interactors.dtos import *


class CreateBankRequestDTOFactory(factory.Factory):
    class Meta:
        model = CreateBankRequestDTO

    bank_name = factory.Sequence(lambda n: f'Bank {n}')
    ifsc_code = factory.Sequence(lambda n: f'IFSC{n}')
    bank_manager_email = factory.Sequence(lambda n: f'BankManager{n}@gmail.com')
    branch = 'ALLGADDA'


class CreateBankResponseDTOFactory(factory.Factory):
    class Meta:
        model = CreateBankResponseDTO

    bank_id = 1
    manager_id = 1


class CreateAccountRequestDTOFactory(factory.Factory):
    class Meta:
        model = CreateAccountRequestDTO

    bank_id = factory.SubFactory(CreateBankRequestDTOFactory)
    name = factory.Sequence(lambda n: f'Account {n}')
    age = 20
    mobile_number = '1234567890'


class MakeTransactionRequestDTOFactory(factory.Factory):
    class Meta:
        model = MakeTransactionRequestDTO

    from_account_number = 1
    to_account_number = 2
    amount = 100
    transaction_type = 'DEBIT'


class MakeTransactionResponseDTOFactory(factory.Factory):
    class Meta:
        model = MakeTransactionResponseDTO

    transaction_id = 1
    amount_paid = 100
    message = 'SUCCESS'


class GetAllTransactionsQueryParamsDTOFactory(factory.Factory):
    class Meta:
        model = GetAllTransactionsQueryParamsDTO

    limit = 10
    offset = 0
    sort_by = 'date_time'
    type = 'DEBIT'


class TransactionDTOFactory(factory.Factory):
    class Meta:
        model = TransactionDTO

    transaction_id = factory.Sequence(lambda n: n)
    transaction_type = 'DEBIT'
    amount = 100
    date_time = factory.LazyFunction(datetime.datetime.now)
    to_account_id = 1


class SelfTransactionRequestDTOFactory(factory.Factory):
    class Meta:
        model = SelfTransactionRequestDTO

    account_number = 1
    amount = 100
    transaction_type = 'DEBIT'


class UpdateAccountRequestDTOFactory(factory.Factory):
    class Meta:
        model = UpdateAccountRequestDTO

    account_id = 1
    name = 'Account 1'
    age = 20
