import interlagos.generic.stemmer as stemmer

TOKENS = [
    'the', 'body', 'may', 'perhaps', 'compensates', 'for', 'the', 'loss', 'of',
    'a', 'true', 'metaphysics'
]


def test_stem(snapshot):
    stems = stemmer.stem(TOKENS)

    snapshot.assert_match(stems)
