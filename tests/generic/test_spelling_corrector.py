import interlagos.generic.spelling_corrector as spelling_corrector

TOKENS = [
    'the', 'memiry', 'we', 'ued', 'to', 'share', 'is', 'no', 'lnger', 'cohernt'
]


def test_correct(snapshot):
    expected_tokens = [
        'the', 'memory', 'we', 'used', 'to', 'share', 'is', 'no', 'longer',
        'coherent'
    ]
    tokens = spelling_corrector.correct(TOKENS)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)
