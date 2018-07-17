import re


def sanitize(tokens):
    """Remove symbols/punctuation-only tokens

    Args:
        tokens (list of str): A list of tokens.

    Returns:
        list of str: A list of filtered tokens.

    """

    return [token for token in tokens
            if not re.search(r'^\W+$', token)]
