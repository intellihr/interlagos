# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_extract_n_gram_from 1'] = [
    'cats',
    'are',
    'good',
    'pets',
    'for',
    'they',
    'are',
    'clean',
    'and',
    'are',
    'not',
    'noisy',
    'cats are',
    'are good',
    'good pets',
    'pets for',
    'for they',
    'they are',
    'are clean',
    'clean and',
    'and are',
    'are not',
    'not noisy',
    'cats are good',
    'are good pets',
    'good pets for',
    'pets for they',
    'for they are',
    'they are clean',
    'are clean and',
    'clean and are',
    'and are not',
    'are not noisy'
]

snapshots['test_extract_phrases_from 1'] = [
    'good pets'
]
