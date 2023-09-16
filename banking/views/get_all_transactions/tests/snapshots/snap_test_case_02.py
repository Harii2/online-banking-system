# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetAllTransactionsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetAllTransactionsAPITestCase::test_case body'] = {
    'transactions': [
        {
            'account_id': '2',
            'amount': 100,
            'date_time': '16-09-2023 06:50:52',
            'transaction_id': 1,
            'transaction_type': 'DEBIT'
        }
    ]
}

snapshots['TestCase02GetAllTransactionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '130',
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
