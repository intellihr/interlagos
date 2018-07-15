from interlagos.generic._global import TRANSLATION


def translate(raw_tokens):
    """Attempt to fix incomplete word/token according to
    the key/value in TRANSLATION dictionary.

    Args:
        raw_tokens (list of str): A list of words/tokens.

    Returns:
        list of str: A list of translated tokens
            (inapplicable tokens remain).

    Note:
        The returned tokens will have the same size
        and the same order as the input ones.

    """

    tokens = []
    for raw_token in raw_tokens:
        if raw_token in TRANSLATION:
            tokens += TRANSLATION[raw_token]
        else:
            tokens.append(raw_token)
    return tokens
