# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sanitize 1'] = [
    'if',
    'you',
    'like',
    'tuna',
    'and',
    'tomato',
    'sauce',
    'try',
    'combining',
    'the',
    'two',
    'it',
    "'s",
    'really',
    'not',
    'as',
    'bad',
    'as',
    'it',
    'sounds'
]
