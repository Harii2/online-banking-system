from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.constants.exception_messages import *
from banking.models import Bank, Staff, Account, Transaction
from banking.exceptions.custom_exceptions import *
from banking.interactors.dtos import CreateBankRequestDTO, TransactionHistoryResponseDTO
from banking.interactors.dtos import CreateAccountRequestDTO
from django.db.models import Q
from banking.interactors.dtos import TransactionDTO, TransactionHistoryResponseDTO
from banking.interactors.dtos import *


class StorageImplementation(StorageInterface):
    def account_make_transaction(self, self_transaction_request_dto: SelfTransactionRequestDTO) -> MakeTransactionResponseDTO:
        amount = self_transaction_request_dto.amount
        account_number = self_transaction_request_dto.account_number
        transaction_type = self_transaction_request_dto.transaction_type
        make_transaction_response_dto = MakeTransactionResponseDTO(
            transaction_id=0,
            amount_paid=0,
            message='None'
        )
        if transaction_type == 'CREDIT':
            Account.objects.filter(pk=account_number).update(
                balance=self.get_accountant_balance(account_id=account_number) + amount)
            transaction = Transaction.objects.create(from_account_id_id=account_number, to_account_id_id=account_number,
                                                     amount=amount, type=transaction_type)
            make_transaction_response_dto.transaction_id = transaction.id
            make_transaction_response_dto.amount_paid = transaction.amount
            make_transaction_response_dto.message = 'SUCCESS'
        if transaction_type == 'DEBIT':
            Account.objects.filter(pk=account_number).update(
                balance=self.get_accountant_balance(account_id=account_number) - amount)
            transaction = Transaction.objects.create(from_account_id_id=account_number, to_account_id_id=account_number,
                                                     amount=amount, type=transaction_type)
            make_transaction_response_dto.transaction_id = transaction.id
            make_transaction_response_dto.amount_paid = transaction.amount
            make_transaction_response_dto.message = 'SUCCESS'
        return make_transaction_response_dto

    def validate_debit_user_balance(self, account_id: int, amount: int):
        balance = Account.objects.get(pk=account_id).balance
        if balance < amount:
            raise InsufficientBalance

    def make_transaction(self, make_transaction_dto: MakeTransactionDTO) -> MakeTransactionResponseDTO:
        amount = make_transaction_dto.amount
        from_account_number = make_transaction_dto.from_account_number
        to_account_number = make_transaction_dto.to_account_number
        transaction_type = make_transaction_dto.transaction_type
        make_transaction_response_dto = MakeTransactionResponseDTO(
            transaction_id=0,
            amount_paid=0,
            message='None'
        )
        if transaction_type == 'DEBIT':
            Account.objects.filter(pk=from_account_number).update(
                balance=self.get_accountant_balance(account_id=from_account_number) - amount)
            Account.objects.filter(pk=to_account_number).update(
                balance=self.get_accountant_balance(account_id=to_account_number) + amount)
            transaction = Transaction.objects.create(
                from_account_id_id=from_account_number,
                to_account_id_id=to_account_number,
                amount=amount,
                type=transaction_type
            )
            make_transaction_response_dto.transaction_id = transaction.id
            make_transaction_response_dto.amount_paid = amount
            make_transaction_response_dto.message = 'SUCCESS'
        if transaction_type == 'CREDIT':
            Account.objects.filter(pk=from_account_number).update(
                balance=self.get_accountant_balance(account_id=from_account_number) + amount)
            Account.objects.filter(pk=to_account_number).update(
                balance=self.get_accountant_balance(account_id=to_account_number) - amount)
            transaction = Transaction.objects.create(
                from_account_id_id=from_account_number,
                to_account_id_id=to_account_number,
                amount=amount,
                type=transaction_type
            )
            make_transaction_response_dto.transaction_id = transaction.id
            make_transaction_response_dto.amount_paid = amount
            make_transaction_response_dto.message = 'SUCCESS'
        return make_transaction_response_dto

    def validate_amount(self, amount: int) -> None:
        if amount <= 0:
            raise InvalidAmount

    def get_transaction_history(self, account_id: int,
                                query_params_dto: GetAllTransactionsQueryParamsDTO) -> TransactionHistoryResponseDTO:
        from_acc = Q(from_account_id=account_id)
        to_acc = Q(to_account_id=account_id)
        limit = query_params_dto.limit
        offset = query_params_dto.offset
        type = query_params_dto.type
        sort_by = query_params_dto.sort_by
        order_by = '-date_time' if sort_by == 'DESC' else 'date_time'
        transaction_history = Transaction.objects.filter(from_acc | to_acc).filter(type=type).order_by(order_by)[
                              offset:offset + limit]
        transactions = []
        for transaction in transaction_history:
            trns = TransactionDTO(
                transaction_id=transaction.id,
                transaction_type=transaction.type,
                amount=transaction.amount,
                date_time=transaction.date_time.strftime("%d-%m-%Y %H:%M:%S"),
                to_account_id=transaction.type == transaction.to_account_id_id if transaction.type == 'DEBIT' else transaction.from_account_id_id
            )
            transactions.append(trns)
        transaction_dto_response = TransactionHistoryResponseDTO(
            transaction_history=transactions
        )
        return transaction_dto_response

    def get_accountant_balance(self, account_id: int) -> int:
        balance = Account.objects.get(pk=account_id).balance
        return balance

    def validate_account_id(self, account_id: int) -> None:
        is_exists = Account.objects.filter(id=account_id).exists()
        if not is_exists:
            raise InvalidAccountId

    def validate_ifsc_code(self, ifsc_code: str) -> None:
        is_exists = Bank.objects.filter(ifsc_code=ifsc_code).exists()
        if is_exists:
            raise IFSCCodeAlreadyExists

    def manager_already_exists(self, manager_email: str):
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

    def validate_bank_id(self, bank_id: int):
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
