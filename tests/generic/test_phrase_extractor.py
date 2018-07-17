import interlagos.generic.phrase_extractor as phrase_extractor

TOKENS = [
    'cats', 'are', 'good', 'pets', 'for', 'they', 'are', 'clean', 'and', 'are',
    'not', 'noisy'
]


def test_extract_n_gram_from(snapshot):
    n_grams = phrase_extractor.extract_n_gram_from(TOKENS)

    snapshot.assert_match(n_grams)


def test_extract_phrases_from(snapshot):
    phrases = phrase_extractor.extract_phrases_from(TOKENS, lambda x: x)

    snapshot.assert_match(phrases)
