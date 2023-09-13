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
    def get_delete_account_response(self, deleted: str):
        response_dict = {
            "message": deleted
        }
        return self.prepare_200_success_response(response_dict=response_dict)

    def get_update_account_response(self, updated: bool):
        response_dict = {
            "message": f'UPDATED' if updated else 'NOT UPDATED'
        }
        return self.prepare_200_success_response(response_dict=response_dict)

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
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_invalid_amount(self, *args, **kwargs):
        response_dict = {
            "response": INVALID_AMOUNT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AMOUNT[1],
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def get_transaction_history_response(self,
                                         transaction_history_response_dto: TransactionHistoryResponseDTO) -> HttpResponse:
        print(transaction_history_response_dto.transaction_history)
        transactions = []
        for transaction in transaction_history_response_dto.transaction_history:
            trns = {
                'transaction_id': transaction.transaction_id,
                'transaction_type': transaction.transaction_type,
                'amount': transaction.amount,
                'date_time': transaction.date_time,
                'to_account_id': transaction.to_account_id
            }
            transactions.append(trns)
        transactions_dict = {
            'transactions': transactions
        }
        return self.prepare_200_success_response(response_dict=transactions_dict)

    def raise_invalid_age(self, *args, **kwargs):
        response_dict = {
            "response": INVALID_AGE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_AGE[1],
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_invalid_mobile_number(self, *args, **kwargs):
        response_dict = {
            "response": INVALID_MOBILE_NUMBER[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_MOBILE_NUMBER[1],
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_invalid_user_name(self, *args, **kwargs):
        response_dict = {
            "response": INVALID_USER_NAME[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_NAME[1],
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def get_account_balance_response(self, balance: int) -> Dict[str, int]:
        balance_dict = {'balance': balance}
        return self.prepare_200_success_response(response_dict=balance_dict)

    def raise_invalid_account_id(self, *args, **kwargs):
        response_dict = {
            "response": INVALID_ACCOUNT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ACCOUNT_ID[1],
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_ifsc_code_already_exists(self, *args, **kwargs):
        response_dict = {
            "response": INVALID_IFSC_CODE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_IFSC_CODE[1],
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_manager_email_already_exists(self, *args, **kwargs):
        response_dict = {
            "response": INVALID_MANAGER_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_MANAGER_EMAIL[1],
        }
        return self.prepare_400_bad_request_response(response_dict=response_dict)

    def raise_bank_not_exists(self, *args, **kwargs):
        response_dict = {
            "response": BANK_NOT_EXISTS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": BANK_NOT_EXISTS[1],
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def get_create_bank_response(self, bank_id: int, manager_id: int):
        create_bank_response = {
            'bank_id': bank_id,
            'manager_id': manager_id
        }
        return self.prepare_201_created_response(response_dict=create_bank_response)

    def get_create_account_response(self, account_number: int) -> Dict[str, int]:
        account_number_dict = {'account_number': account_number}
        return self.prepare_201_created_response(response_dict=account_number_dict)
