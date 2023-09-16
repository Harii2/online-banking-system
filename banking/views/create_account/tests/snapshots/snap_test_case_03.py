# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03CreateAccountAPITestCase::test_case status'] = 400

snapshots['TestCase03CreateAccountAPITestCase::test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_MOBILE_NUMBER',
    'response': 'Mobile Number must be 10 digit words'
}

snapshots['TestCase03CreateAccountAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '111',
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
