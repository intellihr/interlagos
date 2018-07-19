from interlagos.generic import tokenizer

PARAGRAPH = 'Aliqua velit fugiat labore dolor incididunt labore. ' \
    'Id pariatur commodo non minim. ' \
    'Est esse ipsum sit exercitation dolor commodo. ' \
    'Adipisicing deserunt pariatur fugiat laboris ut reprehenderit.'

SENTENCE = 'Proident aute minim exercitation pariatur irure ullamco mollit.'


def test_sentensize(snapshot):
    expected_sentences = [
        'Aliqua velit fugiat labore dolor incididunt labore.',
        'Id pariatur commodo non minim.',
        'Est esse ipsum sit exercitation dolor commodo.',
        'Adipisicing deserunt pariatur fugiat laboris ut reprehenderit.'
    ]
    sentences = tokenizer.sentensize(PARAGRAPH)

    assert sentences == expected_sentences

    snapshot.assert_match(sentences)


def test_tokenize(snapshot):
    expected_tokens = [
        'Proident', 'aute', 'minim', 'exercitation', 'pariatur', 'irure',
        'ullamco', 'mollit', '.'
    ]
    tokens = tokenizer.tokenize(SENTENCE)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)
