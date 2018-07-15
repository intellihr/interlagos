from interlagos.generic._global import STOPWORDS


def remove_from(tokens):
    """Remove tokens that are in the STOPWORDS list

    Todo:
        * Support customizable stopword list.

    Args:
        tokens (list of str): A list of tokens.

    Returns:
        list of str: A list of filtered tokens.

    """

    return [token for token in tokens if token not in STOPWORDS]
