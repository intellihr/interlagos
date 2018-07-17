# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_sentensize 1'] = [
    'Aliqua velit fugiat labore dolor incididunt labore.',
    'Id pariatur commodo non minim.',
    'Est esse ipsum sit exercitation dolor commodo.',
    'Adipisicing deserunt pariatur fugiat laboris ut reprehenderit.'
]

snapshots['test_tokenize 1'] = [
    'Proident',
    'aute',
    'minim',
    'exercitation',
    'pariatur',
    'irure',
    'ullamco',
    'mollit',
    '.'
]
