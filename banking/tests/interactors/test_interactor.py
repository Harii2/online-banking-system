import json
from unittest.mock import create_autospec
import pytest

from banking.interactors.delete_account import DeleteAccountInteractor
from banking.interactors.dtos import GetAllTransactionsQueryParamsDTO
from banking.interactors.get_account_balance_interactor import GetAccountBalanceInteractor
from banking.interactors.get_transaction_history_interactor import GetTransactionHistoryInteractor
from banking.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.interactors.create_bank_interactor import CreateBankInteractor
from banking.interactors.create_account_interactor import CreateAccountInteractor
from banking.interactors.account_make_transaction import AccountMakeTransactionInteractor
from banking.interactors.make_transaction import MakeTransactionInteractor
from django.http import HttpResponse
from banking.exceptions.custom_exceptions import *
from banking.constants.exception_messages import *
from banking.constants.enum import StatusCode
from dataclasses import asdict

from banking.interactors.update_account_interactor import UpdateAccountInteractor
from banking.models import Account
from banking.tests.factories.presenter_dtos import TransactionHistoryResponseDTOFactory
from banking.tests.factories.storage_dtos import CreateBankResponseDTOFactory, CreateBankRequestDTOFactory, \
    CreateAccountRequestDTOFactory, SelfTransactionRequestDTOFactory, MakeTransactionResponseDTOFactory, \
    MakeTransactionRequestDTOFactory, UpdateAccountRequestDTOFactory

pytestmark = pytest.mark.django_db


class TestCreateBank:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter(self):
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture
    def interactor(self, storage):
        interactor = CreateBankInteractor(storage=storage)
        return interactor

    def test_create_bank_with_valid_response(self, storage, interactor, presenter, snapshot):
        # Arrange
        create_bank_response_dto_factory = CreateBankResponseDTOFactory()
        create_account_request_dto_factory = CreateBankRequestDTOFactory()
        storage.create_bank.return_value = (1, 1)
        presenter.get_create_bank_response.return_value = HttpResponse(json.dumps(
            asdict(create_bank_response_dto_factory)
        ), status=201)

        # Act
        actual_response = interactor.create_bank_wrapper(
            create_bank_request_dto=create_account_request_dto_factory,
            presenter=presenter
        )

        # assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Bank created Succesfully ")
        assert storage.create_manager_for_bank.call_count == 1
        assert presenter.get_create_bank_response.call_count == 1
        storage.create_bank.assert_called_once_with(create_bank_request_dto=create_account_request_dto_factory)
        storage.validate_ifsc_code.assert_called_once_with(ifsc_code=create_account_request_dto_factory.ifsc_code)
        storage.manager_already_exists.assert_called_once_with(
            manager_email=create_account_request_dto_factory.bank_manager_email)

    def test_invalid_ifsc_code(self, storage, interactor, presenter, snapshot):
        # Arrange
        create_account_request_dto = CreateBankRequestDTOFactory()
        storage.validate_ifsc_code.side_effect = IFSCCodeAlreadyExists
        presenter.raise_ifsc_code_already_exists.return_value = HttpResponse(json.dumps({
            "response": INVALID_IFSC_CODE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_IFSC_CODE[1],

        }), status=400)

        # Act
        response = interactor.create_bank_wrapper(
            create_bank_request_dto=create_account_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid IFSC code ")
        assert response_data['http_status_code'] == 400
        assert response_data['res_status'] == INVALID_IFSC_CODE[1]
        assert presenter.raise_ifsc_code_already_exists.call_count == 1
        storage.validate_ifsc_code.assert_called_once_with(ifsc_code=create_account_request_dto.ifsc_code)

    def test_create_bank_with_manager_email_already_exists(self, storage, interactor, presenter, snapshot):
        # Arrange
        create_account_request_dto = CreateBankRequestDTOFactory()
        storage.manager_already_exists.side_effect = ManagerEmailAlreadyExists
        presenter.raise_manager_email_already_exists.return_value = HttpResponse(json.dumps({
            "response": INVALID_MANAGER_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_MANAGER_EMAIL[1],

        }), status=400)

        # Act
        response = interactor.create_bank_wrapper(
            create_bank_request_dto=create_account_request_dto,
            presenter=presenter
        )

        # Assert
        response = json.loads(response.content)
        snapshot.assert_match(response, "Manager email already exists")
        assert response['http_status_code'] == 400
        assert response['res_status'] == INVALID_MANAGER_EMAIL[1]
        assert storage.manager_already_exists.call_count == 1
        assert presenter.raise_manager_email_already_exists.call_count == 1
        storage.manager_already_exists.assert_called_once_with(
            manager_email=create_account_request_dto.bank_manager_email)

    @pytest.fixture
    def interactor_create_account(self, storage):
        interactor = CreateAccountInteractor(storage=storage)
        return interactor

    def test_create_account_with_invalid_bank_id(self, storage, interactor_create_account, presenter, snapshot):
        # Arrange
        create_account_request_dto = CreateAccountRequestDTOFactory()
        storage.validate_bank_id.side_effect = BankNotExists
        presenter.raise_bank_not_exists.return_value = HttpResponse(json.dumps({
            "response": BANK_NOT_EXISTS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": BANK_NOT_EXISTS[1],
        }))

        # Act
        response = interactor_create_account.create_account_wrapper(
            create_account_request_dto=create_account_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Bank Not Exists")
        storage.validate_bank_id.assert_called_once_with(bank_id=create_account_request_dto.bank_id)
        presenter.raise_bank_not_exists.assert_called_once_with()

    def test_create_account_with_invalid_accountant_name(self, storage, interactor_create_account, presenter, snapshot):
        # Arrange
        create_account_request_dto = CreateAccountRequestDTOFactory()
        storage.validate_user_details.side_effect = InvalidAccountantName
        presenter.raise_invalid_user_name.return_value = HttpResponse(json.dumps({
            "response": INVALID_USER_NAME[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_NAME[1],
        }))

        # Act
        response = interactor_create_account.create_account_wrapper(
            create_account_request_dto=create_account_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Accountant Name")
        presenter.raise_invalid_user_name.assert_called_once_with()
        storage.validate_user_details.assert_called_once_with(
            create_account_request_dto=create_account_request_dto
        )

    def test_create_account_with_invalid_age(self, storage, interactor_create_account, presenter, snapshot):
        # Arrange
        create_account_request_dto = CreateAccountRequestDTOFactory()
        storage.validate_user_details.side_effect = InvalidAge
        presenter.raise_invalid_age.return_value = HttpResponse(json.dumps({
            "response": INVALID_AGE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AGE[1],
        }))
        # Act
        response = interactor_create_account.create_account_wrapper(
            create_account_request_dto=create_account_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Age")
        presenter.raise_invalid_age.assert_called_once_with()
        storage.validate_user_details.assert_called_once_with(
            create_account_request_dto=create_account_request_dto
        )

    def test_create_account_with_invalid_mobile_number(self, storage, interactor_create_account, presenter, snapshot):
        # Arrange
        create_account_request_dto = CreateAccountRequestDTOFactory()
        storage.validate_user_details.side_effect = InvalidMobileNumber
        presenter.raise_invalid_mobile_number.return_value = HttpResponse(json.dumps({
            "response": INVALID_MOBILE_NUMBER[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_MOBILE_NUMBER[1],
        }))
        # Act
        response = interactor_create_account.create_account_wrapper(
            create_account_request_dto=create_account_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Mobile Number")
        presenter.raise_invalid_mobile_number.assert_called_once_with()
        storage.validate_user_details.assert_called_once_with(
            create_account_request_dto=create_account_request_dto
        )

    def test_create_account_with_valid_account_details(self, storage, interactor_create_account, presenter, snapshot):
        # Arrange
        create_account_request_dto = CreateAccountRequestDTOFactory()
        storage.create_account.return_value = 1
        presenter.get_create_account_response.return_value = HttpResponse(json.dumps({
            "account_number": 1
        }))

        # Act
        response = interactor_create_account.create_account_wrapper(
            create_account_request_dto=create_account_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Account Created Succesfully ")
        storage.create_account.assert_called_once_with(create_account_request_dto=create_account_request_dto)
        storage.validate_bank_id.assert_called_once_with(bank_id=create_account_request_dto.bank_id)
        storage.validate_user_details.assert_called_once_with(create_account_request_dto=create_account_request_dto)
        storage.create_account.assert_called_once_with(create_account_request_dto=create_account_request_dto)
        presenter.get_create_account_response.assert_called_once_with(account_number=1)

    @pytest.fixture
    def interactor_account_make_transaction(self, storage):
        interactor = AccountMakeTransactionInteractor(storage=storage)
        return interactor

    def test_account_make_transaction_with_invalid_account_number(self, storage, interactor_account_make_transaction,
                                                                  presenter,
                                                                  snapshot):
        # Arrange
        self_transaction_request_dto = SelfTransactionRequestDTOFactory()
        storage.validate_account_id.side_effect = InvalidAccountId
        presenter.raise_invalid_account_id.return_value = HttpResponse(json.dumps({
            "response": INVALID_ACCOUNT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ACCOUNT_ID[1]
        }))

        # Act
        response = interactor_account_make_transaction.account_make_transaction_wrapper(
            self_transaction_request_dto=self_transaction_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Account Id")
        presenter.raise_invalid_account_id.assert_called_once_with()
        storage.validate_account_id.assert_called_once_with(account_id=self_transaction_request_dto.account_number)

    def test_account_make_transaction_with_invalid_amount(self, storage, interactor_account_make_transaction, presenter,
                                                          snapshot):
        # Arrange
        self_transaction_request_dto = SelfTransactionRequestDTOFactory()
        storage.validate_amount.side_effect = InvalidAmount
        presenter.raise_invalid_amount.return_value = HttpResponse(json.dumps({
            "response": INVALID_AMOUNT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AMOUNT[1]
        }))

        # Act
        response = interactor_account_make_transaction.account_make_transaction_wrapper(
            self_transaction_request_dto=self_transaction_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Amount")
        presenter.raise_invalid_amount.assert_called_once_with()
        storage.validate_amount.assert_called_once_with(amount=self_transaction_request_dto.amount)

    def test_account_make_transaction_with_insufficient_balance(self, storage, interactor_account_make_transaction,
                                                                presenter,
                                                                snapshot):
        # Arrange
        self_transaction_request_dto = SelfTransactionRequestDTOFactory()
        storage.validate_amount.side_effect = InsufficientBalance
        presenter.raise_insufficient_balance.return_value = HttpResponse(json.dumps({
            "response": INVALID_AMOUNT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AMOUNT[1]
        }))

        # Act
        response = interactor_account_make_transaction.account_make_transaction_wrapper(
            self_transaction_request_dto=self_transaction_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Insufficient Balance")
        presenter.raise_insufficient_balance.assert_called_once_with()
        storage.validate_amount.assert_called_once_with(amount=self_transaction_request_dto.amount)

    def test_account_make_transaction_with_valid_transaction(self, storage, interactor_account_make_transaction,
                                                             presenter, snapshot):
        # Arrange
        self_transaction_request_dto = SelfTransactionRequestDTOFactory()
        make_transaction_response_dto = MakeTransactionResponseDTOFactory()
        storage.account_make_transaction.return_value = make_transaction_response_dto
        presenter.get_make_transaction_response.return_value = HttpResponse(
            json.dumps(asdict(make_transaction_response_dto)))

        # Act
        response = interactor_account_make_transaction.account_make_transaction_wrapper(
            self_transaction_request_dto=self_transaction_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Account Transaction Successful")
        storage.account_make_transaction.assert_called_once_with(
            self_transaction_request_dto=self_transaction_request_dto
        )
        presenter.get_make_transaction_response.assert_called_once_with(
            make_transaction_response_dto=make_transaction_response_dto
        )
        storage.validate_account_id.assert_called_once_with(account_id=self_transaction_request_dto.account_number)
        presenter.raise_invalid_account_id.assert_not_called()
        presenter.raise_insufficient_balance.assert_not_called()
        storage.validate_account_id.assert_called_once_with(account_id=self_transaction_request_dto.account_number)
        storage.validate_amount.assert_called_once_with(amount=self_transaction_request_dto.amount)

    @pytest.fixture
    def interactor_make_transaction(self, storage):
        interactor = MakeTransactionInteractor(storage=storage)
        return interactor

    def test_make_transaction_with_invalid_account_number(self, storage, interactor_make_transaction, presenter,
                                                          snapshot):
        # Arrange
        make_transaction_request_dto = MakeTransactionRequestDTOFactory()
        storage.validate_account_id.side_effect = InvalidAccountId
        presenter.raise_invalid_account_id.return_value = HttpResponse(json.dumps({
            "response": INVALID_ACCOUNT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ACCOUNT_ID[1]
        }))

        # Act
        response = interactor_make_transaction.make_transaction_wrapper(
            make_transaction_dto=make_transaction_request_dto,
            presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Account Id")
        storage.validate_account_id.assert_called_once_with(account_id=make_transaction_request_dto.from_account_number)
        presenter.raise_invalid_account_id.assert_called_once_with()

    def test_make_transaction_with_invalid_amount(self, storage, interactor_make_transaction, presenter, snapshot):
        # Arrange
        make_transaction_request_dto = MakeTransactionRequestDTOFactory()
        storage.validate_amount.side_effect = InvalidAmount
        presenter.raise_invalid_amount.return_value = HttpResponse(json.dumps({
            "response": INVALID_AMOUNT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AMOUNT[1]
        }))
        # Act
        response = interactor_make_transaction.make_transaction_wrapper(
            make_transaction_dto=make_transaction_request_dto,
            presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Amount")
        presenter.raise_invalid_amount.assert_called_once_with()
        storage.validate_amount.assert_called_once_with(amount=make_transaction_request_dto.amount)

    def test_make_transaction_with_validating_debit_users_balance(self, storage, interactor_make_transaction, presenter,
                                                                  snapshot):
        # Arrange
        make_transaction_request_dto = MakeTransactionRequestDTOFactory()
        storage.validate_amount.side_effect = InsufficientBalance
        presenter.raise_insufficient_balance.return_value = HttpResponse(json.dumps({
            "response": INVALID_AMOUNT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AMOUNT[1]
        }))
        # Act
        response = interactor_make_transaction.make_transaction_wrapper(
            make_transaction_dto=make_transaction_request_dto,
            presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Insufficient Balance")
        presenter.raise_insufficient_balance.assert_called_once_with()
        storage.validate_amount.assert_called_once_with(amount=make_transaction_request_dto.amount)
        presenter.raise_insufficient_balance.assert_called_once_with()

    def test_make_transaction_with_valid_transaction(self, storage, interactor_make_transaction, presenter, snapshot):
        # Arrange
        make_transaction_request_dto = MakeTransactionRequestDTOFactory()
        make_transaction_response_dto = MakeTransactionResponseDTOFactory()
        storage.make_transaction.return_value = make_transaction_response_dto
        presenter.get_make_transaction_response.return_value = HttpResponse(
            json.dumps(asdict(make_transaction_response_dto)))
        # Act
        response = interactor_make_transaction.make_transaction_wrapper(
            make_transaction_dto=make_transaction_request_dto,
            presenter=presenter
        )

        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Account Transaction Successful")
        storage.make_transaction.assert_called_once_with(
            make_transaction_dto=make_transaction_request_dto
        )
        presenter.get_make_transaction_response.assert_called_once_with(
            make_transaction_response_dto=make_transaction_response_dto
        )
        presenter.raise_invalid_account_id.assert_not_called()
        presenter.raise_insufficient_balance.assert_not_called()
        storage.validate_amount.assert_called_once_with(amount=make_transaction_request_dto.amount)

    @pytest.fixture
    def get_balance_interactor(self, storage):
        interactor = GetAccountBalanceInteractor(storage=storage)
        return interactor

    def test_get_account_balance_with_invalid_account_id(self, storage, get_balance_interactor, presenter,
                                                         snapshot):
        # Arrange
        storage.validate_account_id.side_effect = InvalidAccountId
        presenter.raise_invalid_account_id.return_value = HttpResponse(json.dumps({
            "response": INVALID_ACCOUNT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ACCOUNT_ID[1]
        }))
        # Act
        response = get_balance_interactor.get_accountant_balance_wrapper(
            account_id=1, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Account Id")
        presenter.raise_invalid_account_id.assert_called_once_with()
        storage.validate_account_id.assert_called_once_with(account_id=1)

    def test_get_account_balance_with_valid_account_id(self, get_balance_interactor, storage, presenter, snapshot):
        # Arrange
        storage.get_accountant_balance.return_value = 100
        presenter.get_account_balance_response.return_value = HttpResponse(json.dumps({
            "balance": 100
        }))
        # Act
        response = get_balance_interactor.get_accountant_balance_wrapper(
            account_id=1, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Account Balance")
        storage.get_accountant_balance.assert_called_once_with(account_id=1)
        presenter.get_account_balance_response.assert_called_once_with(balance=100)

    @pytest.fixture
    def update_account_interactor(self, storage):
        interactor = UpdateAccountInteractor(storage=storage)
        return interactor

    def test_update_account_with_invalid_account_id(self, storage, update_account_interactor, presenter, snapshot):
        # Arrange
        update_account_dto = UpdateAccountRequestDTOFactory()
        storage.validate_account_id.side_effect = InvalidAccountId
        presenter.raise_invalid_account_id.return_value = HttpResponse(json.dumps({
            "response": INVALID_ACCOUNT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ACCOUNT_ID[1]
        }))
        # Act
        response = update_account_interactor.update_account_wrapper(
            update_account_dto=update_account_dto, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Account Id")
        presenter.raise_invalid_account_id.assert_called_once_with()
        storage.validate_account_id.assert_called_once_with(account_id=update_account_dto.account_id)

    def test_update_account_with_invalid_name(self, storage, update_account_interactor, presenter, snapshot):
        # Arrange
        update_account_dto = UpdateAccountRequestDTOFactory()
        storage.validate_user_name.side_effect = InvalidAccountantName
        presenter.raise_invalid_user_name.return_value = HttpResponse(json.dumps({
            "response": INVALID_USER_NAME[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_NAME[1]
        }))
        # Act
        response = update_account_interactor.update_account_wrapper(
            update_account_dto=update_account_dto, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid User Name")
        presenter.raise_invalid_user_name.assert_called_once_with()
        storage.validate_user_name.assert_called_once_with(name=update_account_dto.name)

    def test_update_account_with_invalid_age(self, storage, update_account_interactor
                                             , presenter, snapshot):
        # Arrange
        update_account_dto = UpdateAccountRequestDTOFactory()
        storage.validate_user_age.side_effect = InvalidAge
        presenter.raise_invalid_age.return_value = HttpResponse(json.dumps({
            "response": INVALID_AGE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AGE[1]
        }))
        # Act
        response = update_account_interactor.update_account_wrapper(
            update_account_dto=update_account_dto, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Age")
        presenter.raise_invalid_age.assert_called_once_with()
        storage.validate_user_age.assert_called_once_with(age=update_account_dto.age)

    def test_update_account_with_valid_details(self, storage, update_account_interactor, presenter, snapshot):
        # Arrange
        update_account_dto = UpdateAccountRequestDTOFactory()
        storage.update_account_details.return_value = "UPDATED"
        presenter.get_update_account_response.return_value = HttpResponse(
            json.dumps({
                "message": "UPDATED"
            }))
        # Act
        response = update_account_interactor.update_account_wrapper(
            update_account_dto=update_account_dto, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Account Updated")
        storage.update_account_details.assert_called_once_with(
            update_account_dto=update_account_dto
        )
        presenter.get_update_account_response.assert_called_once_with(
            updated="UPDATED"
        )

    @pytest.fixture
    def delete_account_interactor(self, storage):
        interactor = DeleteAccountInteractor(storage=storage)
        return interactor

    def test_delete_account_with_invalid_account_id(self, storage, delete_account_interactor, presenter, snapshot):
        # Arrange
        storage.validate_account_id.side_effect = InvalidAccountId
        presenter.raise_invalid_account_id.return_value = HttpResponse(json.dumps({
            "response": INVALID_ACCOUNT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ACCOUNT_ID[1]
        }))
        # Act
        response = delete_account_interactor.delete_account_wrapper(
            account_id=1, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Account Id")
        presenter.raise_invalid_account_id.assert_called_once_with()
        storage.validate_account_id.assert_called_once_with(account_id=1)

    def test_delete_account_with_valid_account_id(self, delete_account_interactor, storage, presenter, snapshot):
        # Arrange
        storage.delete_account.return_value = "DELETED"
        presenter.get_delete_account_response.return_value = HttpResponse(json.dumps({
            "message": "DELETED"
        }))
        # Act
        response = delete_account_interactor.delete_account_wrapper(
            account_id=1, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Account Deleted")
        storage.delete_account.assert_called_once_with(account_id=1)
        presenter.get_delete_account_response.assert_called_once_with(deleted="DELETED")

    @pytest.fixture
    def get_transaction_history_interactor(self, storage):
        interactor = GetTransactionHistoryInteractor(storage=storage)
        return interactor

    def test_get_transaction_history_with_invalid_account_id(self, storage, get_transaction_history_interactor, presenter, snapshot):
        # Arrange
        storage.validate_account_id.side_effect = InvalidAccountId
        presenter.raise_invalid_account_id.return_value = HttpResponse(json.dumps({
            "response": INVALID_ACCOUNT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ACCOUNT_ID[1]
        }))
        # Act
        response = get_transaction_history_interactor.get_transaction_history_wrapper(
            account_id=1, query_params_dto=GetAllTransactionsQueryParamsDTO(), presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        snapshot.assert_match(response_data, "Invalid Account Id")
        presenter.raise_invalid_account_id.assert_called_once_with()
        storage.validate_account_id.assert_called_once_with(account_id=1)

    def test_get_transaction_history_with_valid_details(self, storage, get_transaction_history_interactor, presenter, snapshot):
        # Arrange
        transaction_dto_response = TransactionHistoryResponseDTOFactory()
        storage.get_transaction_history.return_value = transaction_dto_response
        transactions = []
        for transaction in transaction_dto_response.transaction_history:
            trns = {
                'transaction_id': transaction.transaction_id,
                'transaction_type': transaction.transaction_type,
                'amount': transaction.amount,
                'date_time': transaction.date_time.strftime("%d-%m-%Y %H:%M:%S"),
                'account_id': transaction.account_id
            }
            transactions.append(trns)
        transactions_dict = {
            'transactions': transactions
        }
        query_params_dto = GetAllTransactionsQueryParamsDTO()
        presenter.get_transaction_history_response.return_value = HttpResponse(
            json.dumps(transactions_dict)
        )
        # Act
        response = get_transaction_history_interactor.get_transaction_history_wrapper(
            account_id=1, query_params_dto=query_params_dto, presenter=presenter
        )
        # Assert
        response_data = json.loads(response.content)
        # snapshot.assert_match(response_data, "Transaction History")
        storage.get_transaction_history.assert_called_once_with(
            account_id=1, query_params_dto=query_params_dto
        )

