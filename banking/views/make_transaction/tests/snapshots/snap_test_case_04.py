# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04MakeTransactionAPITestCase::test_case status'] = 400

snapshots['TestCase04MakeTransactionAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INSUFFICIENT_BALANCE',
    'response': 'InSufficient Funds in debit account'
}

snapshots['TestCase04MakeTransactionAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '109',
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
