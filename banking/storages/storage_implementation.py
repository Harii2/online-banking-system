from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.constants.exception_messages import *
from banking.models import Bank, Staff, Account
from banking.exceptions.custom_exceptions import *


class StorageImplementation(StorageInterface):
    def get_accountant_balance(self, account_id: int) -> int:
        balance = Account.objects.get(pk=account_id).balance
        print("Balance in get_account_balance: ", balance)
        return balance

    def validate_account_id(self, account_id: int) -> None:
        is_exists = Account.objects.filter(id=account_id).exists()
        if not is_exists:
            raise InvalidAccountId

    def validate_ifsc_code(self, ifsc_code: str) -> None:
        is_exists = Bank.objects.filter(ifsc_code=ifsc_code).exists()
        if is_exists:
            raise IFSCCodeAlreadyExists

    def is_manager_already_exists(self, manager_email: str):
        is_exists = Staff.objects.filter(email=manager_email).exists()
        if is_exists:
            raise ManagerEmailAlreadyExists

    def create_manager_for_bank(self, bank_id: int, manager_email: str) -> Staff:
        manager = Staff.objects.create(
            name=manager_email,
            email=manager_email,
            mobile_number="",
            role="MANAGER",
            bank_id=bank_id
        )
        return manager

    def create_bank(self, bank_name: str, ifsc_code: str, bank_manager_email: str, branch: str):
        bank = Bank.objects.create(
            name=bank_name,
            ifsc_code=ifsc_code,
            branch=branch
        )
        return bank

    def is_valid_bank_id(self, bank_id: int):
        is_exists = Bank.objects.filter(id=bank_id).exists()
        if not is_exists:
            raise BankNotExists

    def validate_user_details(self, name: str, age: int, mobile_number: str):
        if name.strip() == "" or age == 0 or mobile_number.strip() == "":
            raise InvalidUserDetails

    def create_account(self, bank_id: int, name: str, age: int, mobile_number: str) -> Account:
        bank = Bank.objects.get(pk=bank_id)
        account = Account.objects.create(
            name=name,
            age=age,
            mobile_number=mobile_number,
            bank_id=bank
        )
        return account
