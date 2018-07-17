import itertools

import interlagos.generic.translater as translater
from interlagos.generic._global import TRANSLATION

TOKENS = [
    'ca', "n't", "'m", "'s", "'ve", 'ha', 'wo', 'atm', 'xmas', "'ll", 'im'
]


def test_translate(snapshot):
    tokens = translater.translate(TOKENS)

    snapshot.assert_match(TOKENS)
    snapshot.assert_match(tokens)

    translated_tokens = list(TRANSLATION.values())
    expected_tokens = list(itertools.chain(*translated_tokens))

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)
