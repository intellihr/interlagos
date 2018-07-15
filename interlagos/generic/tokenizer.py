import nltk


def sentensize(text):
    """Break a text into sentences.

    Args:
        text (str): A text containing sentence(s).

    Returns:
        list of str: A list of sentences.

    """

    return nltk.tokenize.sent_tokenize(text)


def tokenize(text):
    """Break a text into tokens.

    Args:
        text (str): A supposedly-sentence text containing word(s).

    Returns:
        list of str: A list of tokens, each of which is a word.

    """

    return nltk.tokenize.word_tokenize(text)
