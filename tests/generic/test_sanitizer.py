from interlagos.generic import sanitizer

TOKENS = [
    'if', 'you', 'like', 'tuna', 'and', 'tomato', 'sauce', '-', 'try',
    'combining', 'the', 'two', '.', 'it', '\'s', 'really', 'not', 'as', 'bad',
    'as', 'it', 'sounds', '.'
]


def test_sanitize(snapshot):
    expected_tokens = [
        'if', 'you', 'like', 'tuna', 'and', 'tomato', 'sauce', 'try',
        'combining', 'the', 'two', 'it', '\'s', 'really', 'not', 'as', 'bad',
        'as', 'it', 'sounds'
    ]
    tokens = sanitizer.sanitize(TOKENS)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)
