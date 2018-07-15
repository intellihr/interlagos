import re

from autocorrect import spell


def correct(tokens):
    """Attempt to fix spelling issue in each token.

    Todo:
        * Convert to using synset instead.
        * Deal with token with symbol/punctuation.

    Args:
        tokens (list of str): A list of tokens.

    Returns:
        list of str: A list of fixed? tokens.

    """

    return [spell(token)
            if not re.search(r'^\W+$', token)
            else token
            for token in tokens]
