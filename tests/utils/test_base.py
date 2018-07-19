import interlagos.utils.base as utils


def test_flatten(snapshot):
    subject = [['a', 'b'], ['c', 'd']]

    expected_tokens = ['a', 'b', 'c', 'd']
    tokens = utils.flatten(subject)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)


def test_replace_with_phrases(snapshot):
    subject = [
        'amet', 'in', 'veniam', 'esse', 'nulla', 'nostrud', 'adipisicing'
    ]
    phrases = ['veniam esse', 'nulla nostrud']

    expected_tokens = [
        'amet', 'in', 'veniam esse', 'nulla nostrud', 'adipisicing'
    ]
    tokens = utils.replace_with_phrases(subject, phrases)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)


def test_append_with_phrases(snapshot):
    subject = [
        'amet', 'in', 'veniam', 'esse', 'nulla', 'nostrud', 'adipisicing'
    ]
    phrases = ['veniam esse', 'nulla nostrud']

    expected_tokens = [
        'amet', 'in', 'veniam', 'esse', 'nulla', 'nostrud', 'adipisicing',
        'veniam esse', 'nulla nostrud'
    ]
    tokens = utils.append_with_phrases(subject, phrases)

    assert tokens == expected_tokens

    snapshot.assert_match(tokens)
