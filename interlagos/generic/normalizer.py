def normalize(tokens):
    """Make all tokens lowercase

    Args:
        tokens (list of str): A list of tokens.

    Returns:
        list of str: A list of tokens in lowercase.

    """

    return [token.lower()
            for token in tokens]
