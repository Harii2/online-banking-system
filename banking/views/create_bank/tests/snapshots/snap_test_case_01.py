# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateBankAPITestCase::test_case status'] = 400

snapshots['TestCase01CreateBankAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IFSC_CODE',
    'response': 'IFSC_code already exists'
}

snapshots['TestCase01CreateBankAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '95',
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
