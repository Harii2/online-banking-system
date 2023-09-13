import json

import pytest
from banking.presenters.presenter_implementation import PresenterImplementation
from banking.constants.exception_messages import *
from banking.constants.enum import StatusCode
from django.http import HttpResponse

pytestmark = pytest.mark.django_db


class TestPresenter:
    @pytest.fixture
    def presenter(self):
        presenter = PresenterImplementation()
        return presenter

    def test_get_create_bank_response(self, presenter):
        bank_id = 1
        manager_id = 1
        expected_response = HttpResponse(json.dumps({
            "bank_id": bank_id,
            "manager_id": manager_id
        }), status=201)
        actual_response = presenter.get_create_bank_response(bank_id, manager_id)
        assert actual_response.content == expected_response.content
        assert actual_response.status_code == expected_response.status_code

    def test_get_account_ifsc_code_already_exists_exception_response(self, presenter):
        expected_response = HttpResponse(json.dumps({
            "response": INVALID_IFSC_CODE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_IFSC_CODE[1],
        }), status=400)
        actual_response = presenter.raise_ifsc_code_already_exists()
        assert actual_response.content == expected_response.content
        assert actual_response.status_code == expected_response.status_code

    def test_get_manager_email_already_exists_exception_response(self, presenter):
        expected_response = HttpResponse(json.dumps({
            "response": INVALID_MANAGER_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_MANAGER_EMAIL[1],
        }), status=400)
        response = presenter.raise_manager_email_already_exists()
        assert actual_response.content == expected_response.content
        assert actual_response.status_code == expected_response.status_code