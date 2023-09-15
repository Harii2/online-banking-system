import datetime

import factory
from banking.models import *


class BankFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bank

    name = factory.Sequence(lambda n: f'Bank {n}')
    ifsc_code = factory.Sequence(lambda n: f'IFSC{n}')
    branch = 'ALLGADDA'
    address = 'Allagadda Main Bazar, Near Allagadda Police Station, Allagadda'
    created_at = factory.LazyFunction(datetime.datetime.now)


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.Sequence(lambda n=1 : f'Account {n}')
    age = 20
    address = 'Allagadda Main Bazar, Near Allagadda Police Station, Allagadda'
    mobile_number = '1234567890'
    created_at = factory.LazyFunction(datetime.datetime.now)
    balance = 1000
    bank = factory.SubFactory(BankFactory)


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    from_account_id = factory.SubFactory(AccountFactory)
    to_account_id = factory.SubFactory(AccountFactory)
    amount = 100
    type = 'DEBIT'
    date_time = factory.LazyFunction(datetime.datetime.now)


class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    name = factory.Sequence(lambda n: f'Staff {n}')
    email = 'a@gmail.com'
    mobile_number = '1234567890'
    joined_at = factory.LazyFunction(datetime.datetime.now)
    role = 'MANAGER'
    bank = factory.SubFactory(BankFactory)

