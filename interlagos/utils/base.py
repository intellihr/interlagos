def flatten(x):
    """Flatten a two-dimensional list into one-dimension.

    Todo:
        * Support flattening n-dimension list into one-dimension.

    Args:
        x (list of list of any): A two-dimension list.

    Returns:
        list of any: An one-dimension list.

    """

    return [a for i in x for a in i]


def replace_with_phrases(tokens, phrases):
    """Replace applicable tokens in semantically-ordered tokens
       with their corresponding phrase.

    Args:
        tokens (list of str): A list of semantically-ordered tokens.
        phrases (list of str): A list of phrases.

    Returns:
        list of str: A list of tokens which applicable tokens
            are replaced with a corresponding phrase.
    Examples:
        >>> print(tokens)
        ['it', 'is', 'straight', 'forward']

        >>> print(phrases)
        ['straight forward']

        >>> print(replace_with_phrases(tokens, phrases))
        ['it', 'is', 'straight forward']

    """

    tempTokens = tokens.copy()
    for phrase in phrases:
        phraseTokens = phrase.split(' ')
        isPhrase = False
        for i in range(len(tempTokens) + 1 - len(phraseTokens)):
            matches = 0
            for key, token in enumerate(phraseTokens):
                if tempTokens[i + key] == token:
                    matches += 1
            if matches == len(phraseTokens):
                isPhrase = True
                break

        if isPhrase:
            start = tempTokens.index(phraseTokens[0])
            end = start + len(phraseTokens)
            tempTokens[start:end] = [' '.join(phraseTokens)]
    return tempTokens


def append_with_phrases(tokens, phrases):
    """Append phrases to the tokens.

    Args:
        tokens (list of str): A list of tokens.
        phrases (list of str): A list of phrases.

    Returns:
        list of str: A concatinated list of tokens and phrases.

    """

    return tokens + phrases
