# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_flatten 1'] = [
    'a',
    'b',
    'c',
    'd'
]

snapshots['test_replace_with_phrases 1'] = [
    'amet',
    'in',
    'veniam esse',
    'nulla nostrud',
    'adipisicing'
]

snapshots['test_append_with_phrases 1'] = [
    'amet',
    'in',
    'veniam',
    'esse',
    'nulla',
    'nostrud',
    'adipisicing',
    'veniam esse',
    'nulla nostrud'
]
