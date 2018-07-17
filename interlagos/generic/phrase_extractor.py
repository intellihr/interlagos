import nltk
import RAKE

from interlagos.generic._global import GRAMMER, STOPWORDS


def extract_n_gram_from(tokens, max_n=3):
    """Compute all shingles starting from 1 to max_n.

    Args:
        tokens (list of str): A list of tokens.
        max_n (int, optional): Highest number of tokens in a shingle.
            Default to 3 (up to tri-gram).

    Returns:
        list of str: A list of shingles.

    """

    output = tokens[:]
    for n in range(2, max_n + 1):
        output += _n_gram(tokens, n)

    return output


def _n_gram(tokens, n=2):
    """Compute n-gram given n from tokens.

    Args:
        tokens (list of str): A list of tokens.
        n (int, optional): Number of tokens in a shingle.
                             Default to 2 (bi-gram).

    Returns:
        list of str: A list of shingles.

    """

    output = []
    for i in range(len(tokens) - n + 1):
        output.append(' '.join(tokens[i:i + n]))
    return output


def extract_phrases_from(tokens, preprocess):
    """Extract phrases from a list of semantically-ordered tokens.

    Args:
        tokens (list of str): A list of semantically-ordered tokens.
        preprocess (callable): A function that pre-processes the extracted
            phrases.

    Returns:
        list of str: A unique set of extracted phrases.

    """

    sentence = ' '.join(tokens)
    rakePhrases = _rake_phrases(sentence, preprocess)
    posPhrases = _pos_phrases(tokens, preprocess)

    # Prioritize RAKE over POS-derived rule-based phrase extraction method
    phrases = list(set(rakePhrases + posPhrases))

    return phrases


def _rake_phrases(text, preprocess):
    """Extract phrases from a text using RAKE algorithm.

    Args:
        text (str): A supposedly-sentence text.
        preprocess (callable): A function that pre-processes the extracted
            phrases.

    Returns:
        list of str: A list of extracted phrases.

    """

    rake = RAKE.Rake(STOPWORDS)

    return [
        preprocess(phrase) for phrase, _ in rake.run(text)
        if len(phrase.split(' ')) > 1
    ]  # phrase only (num_words > 1)


def _pos_phrases(tokens, preprocess):
    """Extract phrases from a text using POS Tagging-derived rule-based approach.

    Args:
        tokens (list of str): A list of semantically-ordered tokens.
        preprocess (callable): A function that pre-processes the extracted
            phrases.

    Returns:
        list of str: A list of extracted phrases.

    """
    chunker = nltk.RegexpParser(GRAMMER)

    posTokens = nltk.tag.pos_tag(tokens)  # apply POS tagging

    # parse the POS-tagged tokens to a tree based on GRAMMAR
    tree = chunker.parse(posTokens)
    return [
        preprocess(' '.join(term)) for term in _get_terms(tree)
        if len(term) > 1
    ]  # phrase only (num_words > 1)


def _get_terms(tree):
    """Get phrases from each leave in POS tree.

    Args:
        tree (nltk.tree.Tree): The parsed POS tree.

    Yields:
        str: The extracted noun/verb phrase.

    """

    for leaf in _get_leaves(tree):
        term = [w for w, _ in leaf]
        yield term


def _get_leaves(tree):
    """Get noun phrases (NP) branch and verb phrases (VP) branch
       from POS tree.

    Args:
        tree (nltk.tree.Tree): The parsed POS tree.

    Yields:
        list of str: A list of phrases marked with either NP/VP.

    """

    for subtree in tree.subtrees(filter=lambda t: t.label() in ['NP', 'VP']):
        yield subtree.leaves()
