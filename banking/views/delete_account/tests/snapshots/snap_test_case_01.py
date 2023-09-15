# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DeleteAccountAPITestCase::test_case status'] = 400

snapshots['TestCase01DeleteAccountAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_ACCOUNT_ID',
    'response': 'User not exists with that account id'
}

snapshots['TestCase01DeleteAccountAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '108',
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
