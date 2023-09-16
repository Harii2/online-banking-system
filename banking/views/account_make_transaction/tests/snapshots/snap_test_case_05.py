# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05AccountMakeTransactionAPITestCase::test_case status'] = 201

snapshots['TestCase05AccountMakeTransactionAPITestCase::test_case body'] = {
    'amount_paid': 100,
    'message': 'SUCCESS',
    'transaction_id': 1
}

snapshots['TestCase05AccountMakeTransactionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '58',
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
