from unittest.mock import create_autospec
import pytest
from banking.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from banking.interactors.storage_interfaces.storage_interface import StorageInterface
from banking.interactors.create_bank_interactor import CreateBankInteractor

from banking.interactors.dtos import CreateBankRequestDTO
from django.http import HttpResponse
from banking.exceptions.custom_exceptions import IFSCCodeAlreadyExists, ManagerEmailAlreadyExists
from banking.constants.exception_messages import *
from banking.constants.enum import StatusCode

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
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

    def test_create_bank_with_valid_response(self, storage, interactor, presenter):
        # Arrange
        expected_response = {
            "bank_id": 1,
            "manager_id": 1
        }
        storage.create_bank.return_value = (1, 1)
        presenter.get_create_bank_response.return_value = expected_response
        create_account_request_dto = CreateBankRequestDTO(
            bank_name="Bank of India",
            ifsc_code="ICIC0000001",
            bank_manager_email="a@gamil.com",
            branch="Mumbai"
        )
        # Act
        actual_response = interactor.create_bank_wrapper(
            create_bank_request_dto=create_account_request_dto,
            presenter=presenter
        )
        # assert
        assert expected_response['bank_id'] == actual_response['bank_id']
        assert expected_response['manager_id'] == actual_response['manager_id']
        assert storage.validate_ifsc_code.call_count == 1
        assert storage.manager_already_exists.call_count == 1
        assert storage.create_bank.call_count == 1
        assert storage.create_manager_for_bank.call_count == 1
        assert presenter.get_create_bank_response.call_count == 1
        storage.create_bank.assert_called_once_with(create_bank_request_dto=create_account_request_dto)
        storage.validate_ifsc_code.assert_called_once_with(ifsc_code="ICIC0000001")
        storage.manager_already_exists.assert_called_once_with(manager_email="a@gamil.com")

    def test_create_bank_with_invalid_ifsc_code(self, storage, interactor, presenter):
        # Arrange
        create_account_request_dto = CreateBankRequestDTO(
            bank_name="Bank of India",
            ifsc_code="ICIC0000001",
            bank_manager_email="a@gamil.com",
            branch="Mumbai"
        )
        storage.validate_ifsc_code.side_effect = IFSCCodeAlreadyExists
        presenter.raise_ifsc_code_already_exists.return_value = {
            "response": INVALID_IFSC_CODE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_IFSC_CODE[1],
        }
        # Act
        response = interactor.create_bank_wrapper(
            create_bank_request_dto=create_account_request_dto,
            presenter=presenter
        )

        print(response)
        assert response['http_status_code'] == 400
        assert response['res_status'] == INVALID_IFSC_CODE[1]
        assert storage.validate_ifsc_code.call_count == 1
        assert presenter.raise_ifsc_code_already_exists.call_count == 1
        storage.validate_ifsc_code.assert_called_once_with(ifsc_code="ICIC0000001")

    def test_create_bank_with_manager_email_already_exists(self, storage, interactor, presenter):
        # Arrange
        create_account_request_dto = CreateBankRequestDTO(
            bank_name="Bank of India",
            ifsc_code="ICIC0000001",
            bank_manager_email="a@gamil.com",
            branch="Mumbai"
        )
        storage.manager_already_exists.side_effect = ManagerEmailAlreadyExists
        presenter.raise_manager_email_already_exists.return_value = {
            "response": INVALID_MANAGER_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_MANAGER_EMAIL[1],
        }
        # Act
        response = interactor.create_bank_wrapper(
            create_bank_request_dto=create_account_request_dto,
            presenter=presenter
        )
        assert response['http_status_code'] == 400
        assert response['res_status'] == INVALID_MANAGER_EMAIL[1]
        assert storage.manager_already_exists.call_count == 1
        assert presenter.raise_manager_email_already_exists.call_count == 1
        storage.manager_already_exists.assert_called_once_with(manager_email="a@gamil.com")
