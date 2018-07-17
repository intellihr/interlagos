from nltk.stem import WordNetLemmatizer


def lemmatize(tokens):
    """Reduce each token to its lemma form by using wordnet.

    Todo:
        * Support customizable lemmatizer

    Args:
        tokens (list of str): A list of tokens.

    Returns:
        list of str: A list of lemmatized tokens.

    """

    wordnet_lemmatizer = WordNetLemmatizer()

    return [wordnet_lemmatizer.lemmatize(token) for token in tokens]
