# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase06MakeTransactionAPITestCase::test_case status'] = 201

snapshots['TestCase06MakeTransactionAPITestCase::test_case body'] = {
    'amount_paid': 1000,
    'message': 'SUCCESS',
    'transaction_id': 1
}

snapshots['TestCase06MakeTransactionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '59',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
