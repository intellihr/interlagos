# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_translate 1'] = [
    'ca',
    "n't",
    "'m",
    "'s",
    "'ve",
    'ha',
    'wo',
    'atm',
    'xmas',
    "'ll",
    'im'
]

snapshots['test_translate 2'] = [
    'can',
    'not',
    'am',
    'is',
    'have',
    'have',
    'will',
    'at',
    'the',
    'moment',
    'Christmas',
    'will',
    'I',
    'am'
]

snapshots['test_translate 3'] = [
    'can',
    'not',
    'am',
    'is',
    'have',
    'have',
    'will',
    'at',
    'the',
    'moment',
    'Christmas',
    'will',
    'I',
    'am'
]
