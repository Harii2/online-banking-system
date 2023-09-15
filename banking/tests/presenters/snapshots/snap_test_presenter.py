# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPresenter.test_get_create_bank_response Bank created Succesfully '] = {
    'bank_id': 1,
    'manager_id': 1
}

snapshots['TestPresenter.test_get_account_ifsc_code_already_exists_exception_response Invalid IFSC code '] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IFSC_CODE',
    'response': 'IFSC_code already exists'
}

snapshots['TestPresenter.test_get_manager_email_already_exists_exception_response Manager email already exists'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_MANAGER_EMAIL',
    'response': 'This Manager already in use or This Mail Already Exists'
}

snapshots['TestPresenter.test_get_create_account_response Account created Succesfully'] = {
    'account_number': 1
}

snapshots['TestPresenter.test_raise_insufficient_balance INSUFFICIENT_BALANCE'] = {
    'http_status_code': 400,
    'res_status': 'INSUFFICIENT_BALANCE',
    'response': 'InSufficient Funds in debit account'
}

snapshots['TestPresenter.test_raise_invalid_amount INVALID_AMOUNT'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AMOUNT',
    'response': 'Amount must be >=1 '
}

snapshots['TestPresenter.test_get_transaction_history_response Getting All Transaction History'] = {
    'transactions': [
        {
            'account_id': 1,
            'amount': 100,
            'date_time': '15-09-2023 11:46:14',
            'transaction_id': 0,
            'transaction_type': 'DEBIT'
        },
        {
            'account_id': 1,
            'amount': 100,
            'date_time': '15-09-2023 11:46:14',
            'transaction_id': 1,
            'transaction_type': 'DEBIT'
        },
        {
            'account_id': 1,
            'amount': 100,
            'date_time': '15-09-2023 11:46:14',
            'transaction_id': 2,
            'transaction_type': 'DEBIT'
        },
        {
            'account_id': 1,
            'amount': 100,
            'date_time': '15-09-2023 11:46:14',
            'transaction_id': 3,
            'transaction_type': 'DEBIT'
        },
        {
            'account_id': 1,
            'amount': 100,
            'date_time': '15-09-2023 11:46:14',
            'transaction_id': 4,
            'transaction_type': 'DEBIT'
        }
    ]
}

snapshots['TestPresenter.test_raise_invalid_age INVALID_AGE'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AGE',
    'response': 'Age must be >=8 years'
}

snapshots['TestPresenter.test_raise_invalid_mobile_number INVALID_MOBILE_NUMBER'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_MOBILE_NUMBER',
    'response': 'Mobile Number must be 10 digit words'
}

snapshots['TestPresenter.test_invalid_user_name INVALID_USER_NAME'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_NAME',
    'response': 'Name is not valid'
}

snapshots['TestPresenter.test_get_account_balance Balance is 1000'] = {
    'balance': 1000
}

snapshots['TestPresenter.test_invalid_account_id Invalid Account ID'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}

snapshots['TestPresenter.test_bank_not_exists_response Bank Not Exists'] = {
    'http_status_code': 400,
    'res_status': 'BANK_NOT_EXISTS',
    'response': 'Bank Not Exists'
}

snapshots['TestPresenter.test_create_account_response Account created Succesfully'] = {
    'account_number': 1
}

snapshots['TestPresenter.test_make_transaction_response Make Transaction'] = {
    'amount_paid': 100,
    'message': 'SUCCESS',
    'transaction_id': 1
}

snapshots['TestPresenter.test_get_update_account_response UPDATED'] = {
    'message': 'UPDATED'
}

snapshots['TestPresenter.test_get_delete_account_response Deleted'] = {
    'message': 'True'
}
