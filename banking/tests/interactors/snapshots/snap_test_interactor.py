# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateBank.test_create_bank_with_valid_response Bank created Succesfully '] = {
    'bank_id': 1,
    'manager_id': 1
}

snapshots['TestCreateBank.test_invalid_ifsc_code Invalid IFSC code '] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IFSC_CODE',
    'response': 'IFSC_code already exists'
}

snapshots['TestCreateBank.test_create_bank_with_manager_email_already_exists Manager email already exists'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_MANAGER_EMAIL',
    'response': 'This Manager already in use or This Mail Already Exists'
}

snapshots['TestCreateBank.test_create_account_with_invalid_bank_id Bank Not Exists'] = {
    'http_status_code': 400,
    'res_status': 'BANK_NOT_EXISTS',
    'response': 'Bank Not Exists'
}

snapshots['TestCreateBank.test_create_account_with_invalid_accountant_name Invalid Accountant Name'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_NAME',
    'response': 'Name is not valid'
}

snapshots['TestCreateBank.test_create_account_with_invalid_age Invalid Age'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AGE',
    'response': 'Age must be >=8 years'
}

snapshots['TestCreateBank.test_create_account_with_invalid_mobile_number Invalid Mobile Number'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_MOBILE_NUMBER',
    'response': 'Mobile Number must be 10 digit words'
}

snapshots['TestCreateBank.test_create_account_with_valid_account_details Account Created Succesfully '] = {
    'account_number': 1
}

snapshots['TestCreateBank.test_account_make_transaction_with_invalid_account_number Invalid Account Id'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}

snapshots['TestCreateBank.test_account_make_transaction_with_invalid_amount Invalid Amount'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AMOUNT',
    'response': 'Amount must be >=1 '
}

snapshots['TestCreateBank.test_account_make_transaction_with_insufficient_balance Insufficient Balance'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AMOUNT',
    'response': 'Amount must be >=1 '
}

snapshots['TestCreateBank.test_account_make_transaction_with_valid_transaction Account Transaction Successful'] = {
    'amount_paid': 100,
    'message': 'SUCCESS',
    'transaction_id': 1
}

snapshots['TestCreateBank.test_make_transaction_with_invalid_account_number Invalid Account Id'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}

snapshots['TestCreateBank.test_make_transaction_with_invalid_amount Invalid Amount'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AMOUNT',
    'response': 'Amount must be >=1 '
}

snapshots['TestCreateBank.test_make_transaction_with_validating_debit_users_balance Insufficient Balance'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AMOUNT',
    'response': 'Amount must be >=1 '
}

snapshots['TestCreateBank.test_make_transaction_with_valid_transaction Account Transaction Successful'] = {
    'amount_paid': 100,
    'message': 'SUCCESS',
    'transaction_id': 1
}

snapshots['TestCreateBank.test_get_account_balance_with_invalid_account_id Invalid Account Id'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}

snapshots['TestCreateBank.test_get_account_balance_with_valid_account_id Account Balance'] = {
    'balance': 100
}

snapshots['TestCreateBank.test_update_account_with_invalid_account_id Invalid Account Id'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}

snapshots['TestCreateBank.test_update_account_with_invalid_name Invalid User Name'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_NAME',
    'response': 'Name is not valid'
}

snapshots['TestCreateBank.test_update_account_with_invalid_age Invalid Age'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_AGE',
    'response': 'Age must be >=8 years'
}

snapshots['TestCreateBank.test_update_account_with_valid_details Account Updated'] = {
    'message': 'UPDATED'
}

snapshots['TestCreateBank.test_delete_account_with_invalid_account_id Invalid Account Id'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}

snapshots['TestCreateBank.test_delete_account_with_valid_account_id Account Deleted'] = {
    'message': 'DELETED'
}

snapshots['TestCreateBank.test_get_transaction_history_with_invalid_account_id Invalid Account Id'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}
