import interlagos.generic.lemmatizer as lemmatizer

TOKENS = [
    'dogs', 'churches', 'leaves', 'aardwolves', 'thesauri', 'millennia',
    'hardrock'
]


def test_lemmatize(snapshot):
    expected_lemmas = [
        'dog', 'church', 'leaf', 'aardwolf', 'thesaurus', 'millennium',
        'hardrock'
    ]
    lemmas = lemmatizer.lemmatize(TOKENS)

    assert lemmas == expected_lemmas

    snapshot.assert_match(lemmas)
