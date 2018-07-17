from nltk.corpus import stopwords

TRANSLATION = {
    'ca': ['can'],
    "n't": ['not'],
    "'m": ['am'],
    "'s": ['is'],
    "'ve": ['have'],
    'ha': ['have'],
    'wo': ['will'],
    'atm': ['at', 'the', 'moment'],
    'xmas': ['Christmas'],
    "'ll": ['will'],
    'im': ['I', 'am']
}

STOPWORDS = stopwords.words('english') + []

GRAMMER = r'''
    NBAR:
        {<NN.*|JJ>*<NN.*>}

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}

    PP:
        {<IN><NP>}

    VP:
        {<VB.*><NP|PP|CLAUSE>+$}

    CLAUSE:
        {<NP><VP>}
'''
