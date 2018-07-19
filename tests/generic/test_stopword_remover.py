from interlagos.generic import stopword_remover

TOKENS = ['to', 'be', 'or', 'not', 'to', 'be']


def test_remove(snapshot):
    expected_tokens = []
    tokens = stopword_remover.remove_from(TOKENS)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)
