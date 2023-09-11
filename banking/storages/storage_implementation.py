from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.constants.exception_messages import *
from banking.models import Bank, Staff, Account
from banking.exceptions.custom_exceptions import *
from banking.interactors.dtos import CreateBankRequestDTO
from banking.interactors.dtos import CreateAccountRequestDTO


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

    def create_manager_for_bank(self, bank_id: int, manager_email: str) -> int:
        manager = Staff.objects.create(
            name=manager_email,
            email=manager_email,
            mobile_number="",
            role="MANAGER",
            bank_id=bank_id
        )
        return manager.id

    def create_bank(self, create_bank_request_dto: CreateBankRequestDTO) -> int:
        bank_name = create_bank_request_dto.bank_name
        ifsc_code = create_bank_request_dto.ifsc_code
        branch = create_bank_request_dto.branch
        bank = Bank.objects.create(
            name=bank_name,
            ifsc_code=ifsc_code,
            branch=branch
        )
        return bank.id

    def is_valid_bank_id(self, bank_id: int):
        is_exists = Bank.objects.filter(id=bank_id).exists()
        if not is_exists:
            raise BankNotExists

    def validate_user_details(self, create_account_request_dto: CreateAccountRequestDTO):
        name = create_account_request_dto.name
        age = create_account_request_dto.age
        mobile_number = create_account_request_dto.mobile_number
        if name.strip() == "":
            raise InvalidAccountantName
        if age < 8:
            raise InvalidAge
        if mobile_number.strip() == "" or len(mobile_number) != 10:
            raise InvalidMobileNumber

    def create_account(self, create_account_request_dto: CreateAccountRequestDTO) -> int:
        name = create_account_request_dto.name
        age = create_account_request_dto.age
        mobile_number = create_account_request_dto.mobile_number
        bank_id = create_account_request_dto.bank_id
        account = Account.objects.create(
            name=name,
            age=age,
            mobile_number=mobile_number,
            bank_id=bank_id
        )
        return account.id
