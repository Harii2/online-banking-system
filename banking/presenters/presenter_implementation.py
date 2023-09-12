import json

from banking.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from banking.constants.exception_messages import *
from typing import Dict
from banking.interactors.dtos import *
from django.http import HttpResponse
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from banking.constants.enum import StatusCode


class PresenterImplementation(PresenterInterface, HTTPResponseMixin):
    def get_make_transaction_response(self, make_transaction_response_dto: MakeTransactionResponseDTO) -> HttpResponse:
        transaction_id = make_transaction_response_dto.transaction_id
        amount_paid = make_transaction_response_dto.amount_paid
        message = make_transaction_response_dto.message
        response = {
            'transaction_id': transaction_id,
            'amount_paid': amount_paid,
            'message': message
        }
        return self.prepare_201_created_response(response_dict=response)

    def raise_insufficient_balance(self, *args, **kwargs):
        response_dict = {
            "response": INSUFFICIENT_BALANCE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INSUFFICIENT_BALANCE[1],
        }
        raise self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_invalid_amount(self, *args, **kwargs):
        raise BadRequest(*INVALID_AMOUNT)

    def get_transaction_history_response(self, transaction_history: TransactionHistoryResponseDTO) -> HttpResponse:
        print(transaction_history.transaction_history)
        transactions = []
        for transaction in transaction_history.transaction_history:
            trns = {
                'transaction_id': transaction.transaction_id,
                'transaction_type': transaction.transaction_type,
                'amount': transaction.amount,
                'date_time': transaction.date_time,
                'to_account_id': transaction.to_account_id
            }
            transactions.append(trns)
        print(transactions)
        json_data = json.dumps(transactions)
        return HttpResponse(json_data, status=200)

    def raise_invalid_age(self, *args, **kwargs):
        raise BadRequest(*INVALID_AGE)

    def raise_invalid_mobile_number(self, *args, **kwargs):
        raise BadRequest(*INVALID_MOBILE_NUMBER)

    def raise_invalid_user_name(self, *args, **kwargs):
        raise BadRequest(*INVALID_USER_NAME)

    def get_account_balance_response(self, balance: int) -> Dict[str, int]:
        balance_dict = {'balance': balance}
        return balance_dict

    def raise_invalid_account_id(self, *args, **kwargs):
        raise BadRequest(*INVALID_ACCOUNT_ID)

    def raise_ifsc_code_already_exists(self, *args, **kwargs):
        raise BadRequest(*INVALID_IFSC_CODE)

    def raise_manager_email_already_exists(self, *args, **kwargs):
        raise BadRequest(*INVALID_MANAGER_EMAIL)

    def raise_bank_not_exists(self, *args, **kwargs):
        raise NotFound(*BANK_NOT_EXISTS)

    def raise_invalid_user_details(self, *args, **kwargs):
        raise BadRequest(*INVALID_USER_DETAILS)

    def get_create_bank_response(self, bank_id: int, manager_id: int) -> CreateBankResponseDTO:
        create_bank_response_dto = CreateBankResponseDTO(bank_id=bank_id, manager_id=manager_id)
        return create_bank_response_dto

    def get_create_account_response(self, account_number: int) -> Dict[str, int]:
        account_number_dict = {'account_number': account_number}
        return account_number_dict
