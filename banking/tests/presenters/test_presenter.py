import json

import pytest
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.constants.exception_messages import *
from banking.constants.enum import StatusCode
from django.http import HttpResponse
from banking.tests.factories.presenter_dtos import TransactionHistoryResponseDTOFactory
import datetime

from banking.tests.factories.storage_dtos import MakeTransactionResponseDTOFactory

pytestmark = pytest.mark.django_db


class TestPresenter:
    @pytest.fixture
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_get_create_bank_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.get_create_bank_response(1, 1)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Bank created Succesfully ")

    def test_get_account_ifsc_code_already_exists_exception_response(self, presenter, snapshot):
        # Act
        actual_response = presenter.raise_ifsc_code_already_exists()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Invalid IFSC code ")

    def test_get_manager_email_already_exists_exception_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_manager_email_already_exists()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Manager email already exists")

    def test_get_create_account_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.get_create_account_response(1)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Account created Succesfully")

    def test_raise_insufficient_balance(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_insufficient_balance()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INSUFFICIENT_BALANCE")

    def test_raise_invalid_amount(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_invalid_amount()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID_AMOUNT")

    def test_get_transaction_history_response(self, presenter, snapshot):
        # Arrange
        transaction_history_response_dto = TransactionHistoryResponseDTOFactory()
        actual_response = presenter.get_transaction_history_response(
            transaction_history_response_dto=transaction_history_response_dto
        )

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Getting All Transaction History")

    def test_raise_invalid_age(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_invalid_age()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID_AGE")

    def test_raise_invalid_mobile_number(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_invalid_mobile_number()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID_MOBILE_NUMBER")

    def test_invalid_user_name(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_invalid_user_name()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "INVALID_USER_NAME")

    def test_get_account_balance(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.get_account_balance_response(balance=1000)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Balance is 1000")

    def test_invalid_account_id(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_invalid_account_id()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Invalid Account ID")

    def test_bank_not_exists_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.raise_bank_not_exists()

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Bank Not Exists")

    def test_create_account_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.get_create_account_response(1)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Account created Succesfully")

    def test_make_transaction_response(self, presenter, snapshot):
        # Arrange
        make_transaction_response_dto = MakeTransactionResponseDTOFactory()
        actual_response = presenter.get_make_transaction_response(
            make_transaction_response_dto=make_transaction_response_dto)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Make Transaction")

    def test_get_update_account_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.get_update_account_response(updated=True)

        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "UPDATED")

    def test_get_delete_account_response(self, presenter, snapshot):
        # Arrange
        actual_response = presenter.get_delete_account_response(deleted="True")
        # Assert
        response_data = json.loads(actual_response.content)
        snapshot.assert_match(response_data, "Deleted")
