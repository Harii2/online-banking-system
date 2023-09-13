import pytest
from banking.models import Bank, Staff
from banking.exceptions.custom_exceptions import IFSCCodeAlreadyExists, ManagerEmailAlreadyExists
from unittest.mock import create_autospec
from banking.interactors.dtos import CreateBankRequestDTO
from banking.storages.storage_implementation import StorageImplementation

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestCreateBank:
    pytestmark = pytest.mark.django_db

    @pytest.fixture
    def storage(self):
        storage = StorageImplementation()
        return storage

    def test_create_bank(self, storage):
        #Arrange
        create_bank_request_dto = CreateBankRequestDTO(
            bank_name="Bank of India",
            ifsc_code="ICIC0000001",
            bank_manager_email="a@gamil.com",
            branch="Mumbai"
        )
        #Act
        actual_bank_id = storage.create_bank(create_bank_request_dto=create_bank_request_dto)
        actual_manager_id = storage.create_manager_for_bank(
            bank_id=actual_bank_id, manager_email="a@gamil.com"
        )
        #Assert
        assert actual_bank_id == 1
        assert actual_manager_id == 1

    def test_create_bank_with_invalid_ifsc_code(self, storage):
        #Arrange
        create_bank_request_dto = CreateBankRequestDTO(
            bank_name="Bank of India",
            ifsc_code="ICIC0000001",
            bank_manager_email="a@gamil.com",
            branch="Mumbai"
        )
        #Act
        bank = storage.create_bank(create_bank_request_dto=create_bank_request_dto)
        #Assert
        with pytest.raises(IFSCCodeAlreadyExists):
            storage.validate_ifsc_code(ifsc_code="ICIC0000001")

    def test_create_bank_with_invalid_manager_email(self, storage):
        #Arrange
        create_bank_request_dto = CreateBankRequestDTO(
            bank_name="Bank of India",
            ifsc_code="ICIC0000001",
            bank_manager_email="a@gamil.com",
            branch="Mumbai"
        )
        #Act
        bank = storage.create_bank(create_bank_request_dto=create_bank_request_dto)
        manager = storage.create_manager_for_bank(bank_id=bank, manager_email="a@gamil.com")
        #Assert
        with pytest.raises(ManagerEmailAlreadyExists):
            storage.manager_already_exists(manager_email="a@gamil.com")
