from nltk.stem.porter import PorterStemmer


def stem(tokens):
    """Reduce each token to its stem form by using Porter stemmer.

    Todo:
        * Support customizable stemmer

    Args:
        tokens (list of str): A list of tokens.

    Returns:
        list of str: A list of stemmed tokens.

    """

    porter_stemmer = PorterStemmer()

    return [porter_stemmer.stem(token) for token in tokens]
