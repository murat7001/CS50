
from nltk.tokenize import sent_tokenize
def lines(a, b):
    """Return lines in both a and b"""
    #TODO
    a_lines = set(a.split("\n"))
    b_lines = set(b.split("\n"))

    return a_lines & b_lines


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    a_sentences = set(sent_tokenize(a))
    b_sentences = set(sent_tokenize(b))

    return a_sentences & b_sentences


def sub_generetor(s, n):
    array = []
    for i in range(len(s) -n+1):
        array.append(s[i:i+n])
    return array

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    a_substrings = set(sub_generetor(a,n))
    b_substrings = set(sub_generetor(b,n))
    return a_substrings & b_substrings