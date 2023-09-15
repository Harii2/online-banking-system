import pytest
from banking.models import Bank, Staff, Account, Transaction
from banking.exceptions.custom_exceptions import *
from banking.storages.storage_implementation import StorageImplementation
from banking.tests.factories.models import BankFactory, StaffFactory, AccountFactory, TransactionFactory
from banking.tests.factories.storage_dtos import CreateBankRequestDTOFactory, CreateAccountRequestDTOFactory, \
    UpdateAccountRequestDTOFactory, MakeTransactionRequestDTOFactory, SelfTransactionRequestDTOFactory, \
    GetAllTransactionsQueryParamsDTOFactory

pytestmark = pytest.mark.django_db


class TestStorageImplementation:

    @pytest.fixture
    def storage(self):
        storage = StorageImplementation()
        return storage

    def test_make_self_transaction(self, storage):
        # Arrange
        acc1 = AccountFactory()
        self_transaction_request_dto = SelfTransactionRequestDTOFactory(account_number=acc1.id)

        # Act
        response = storage.account_make_transaction(self_transaction_request_dto=self_transaction_request_dto)
        # Assert
        acc1 = Account.objects.get(id=acc1.id)
        if self_transaction_request_dto.transaction_type == 'DEBIT':
            assert acc1.balance == (1000 - self_transaction_request_dto.amount)
        else:
            assert acc1.balance == (1000 + self_transaction_request_dto.amount)

    def test_get_transaction_history(self, storage):
        # Arrange
        t1 = TransactionFactory()
        query_params_dto = GetAllTransactionsQueryParamsDTOFactory()

        # Act
        response = storage.get_transaction_history(account_id=1, query_params_dto=query_params_dto)

        # Assert
        acc1 = Account.objects.get(id=1)
        acc2 = Account.objects.get(id=2)
        assert acc2.id == response.transaction_history[0].account_id
        assert t1.type == response.transaction_history[0].transaction_type

    def test_make_transaction(self, storage):
        # Arrange
        acc1 = AccountFactory()
        acc2 = AccountFactory()
        make_transaction_dto = MakeTransactionRequestDTOFactory(from_account_number=acc1.id, to_account_number=acc2.id)

        # Act
        response = storage.make_transaction(make_transaction_dto)
        # Assert
        make_transaction_dto = Transaction.objects.get(id=response.transaction_id)
        acc1 = Account.objects.get(id=acc1.id)
        acc2 = Account.objects.get(id=acc2.id)
        assert make_transaction_dto.id == response.transaction_id
        assert make_transaction_dto.from_account_id_id == acc1.id
        assert make_transaction_dto.to_account_id_id == acc2.id
        if make_transaction_dto.type == 'DEBIT':
            assert acc1.balance == (1000 - make_transaction_dto.amount)
            assert acc2.balance == 1000 + make_transaction_dto.amount
        else:
            assert acc1.balance == (1000 + make_transaction_dto.amount)
            assert acc2.balance == 1000 - make_transaction_dto.amount

    def test_delete_account(self, storage):
        # Arrange
        account = AccountFactory()

        # Act
        storage.delete_account(account_id=account.id)

        # Assert
        assert Account.objects.filter(id=account.id).count() == 0

    def test_update_account_details(self, storage):
        # Arrange
        account = AccountFactory()
        update_account_dto = UpdateAccountRequestDTOFactory(account_id=account.id)

        # Act
        updated = storage.update_account_details(update_account_dto=update_account_dto)
        updated_account_details = Account.objects.get(id=account.id)

        # Assert
        assert updated_account_details.name == update_account_dto.name
        assert updated_account_details.age == update_account_dto.age

    def test_get_balance(self, storage):
        # Arrange
        account = AccountFactory()

        # Act
        balance = storage.get_accountant_balance(account_id=account.id)

        # Assert
        assert balance == account.balance

    def test_create_account(self, storage):
        # Arrange
        bank = BankFactory()
        create_account_request_dto = CreateAccountRequestDTOFactory(bank_id=bank.id)

        # Act
        account_id = storage.create_account(create_account_request_dto=create_account_request_dto)

        # Assert
        account = Account.objects.get(id=account_id)
        assert account.name == create_account_request_dto.name
        assert account.age == create_account_request_dto.age
        assert account.mobile_number == create_account_request_dto.mobile_number

    def test_create_bank(self, storage):
        # Arrange
        create_bank_request_dto = CreateBankRequestDTOFactory()

        # Act
        bank_id = storage.create_bank(create_bank_request_dto=create_bank_request_dto)

        # Assert
        bank = Bank.objects.get(id=bank_id)
        assert bank.name == create_bank_request_dto.bank_name
        assert bank.ifsc_code == create_bank_request_dto.ifsc_code
        assert bank.branch == create_bank_request_dto.branch

    def test_create_manager(self, storage):
        # Arrange
        bank = BankFactory()
        create_bank_request_dto = CreateBankRequestDTOFactory()

        # Act
        manager_id = storage.create_manager_for_bank(bank_id=bank.id,
                                                     manager_email=create_bank_request_dto.bank_manager_email)
        # Assert
        manager = Staff.objects.get(id=manager_id)
        assert manager.email == create_bank_request_dto.bank_manager_email
        assert manager.bank_id == bank.id

    def test_validate_exist_ifsc_code(self, storage):
        # Arrange
        BankFactory(ifsc_code="ICIC0000001")

        # Act
        with pytest.raises(IFSCCodeAlreadyExists):
            storage.validate_ifsc_code(ifsc_code="ICIC0000001")

    def test_validate_manager_email(self, storage):
        # Arrange
        manager_email = "a@gmail.com"
        StaffFactory(email=manager_email, role="MANAGER")

        # Assert
        with pytest.raises(ManagerEmailAlreadyExists):
            storage.manager_already_exists(manager_email=manager_email)

    def test_validate_account_number(self, storage):
        # Arrange
        account_number = 1
        with pytest.raises(InvalidAccountId):
            storage.validate_account_id(account_id=account_number)

    def test_validate_bank_id(self, storage):
        # Arrange
        bank_id = 1
        with pytest.raises(BankNotExists):
            storage.validate_bank_id(bank_id=bank_id)

    def test_validate_name(self, storage):
        name = ""
        with pytest.raises(InvalidAccountantName):
            storage.validate_user_name(name=name)

    def test_validate_age(self, storage):
        age = 6
        with pytest.raises(InvalidAge):
            storage.validate_user_age(age=age)

    def test_validate_debit_user_balance(self, storage):
        account = AccountFactory(balance=200)
        amount = 300
        with pytest.raises(InsufficientBalance):
            storage.validate_debit_user_balance(account_id=account.id, amount=amount)

    def test_validate_amount(self, storage):
        amount = -20
        with pytest.raises(InvalidAmount):
            storage.validate_amount(amount=amount)

    def test_validate_mobile_number(self, storage):
        mobile_number = "123456"
        with pytest.raises(InvalidMobileNumber):
            storage.validate_user_mobile_number(mobile_number=mobile_number)
