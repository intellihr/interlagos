import interlagos.generic.normalizer as normalizer

TOKENS = ['Otherwise', 'IBM', 'intelliHR', 'PoC', 'unknown']


def test_normalize(snapshot):
    expected_tokens = ['otherwise', 'ibm', 'intellihr', 'poc', 'unknown']
    tokens = normalizer.normalize(TOKENS)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)
