"""
DNA sequence consisting of A, C, G, T sequences.
"""
import sys

WEIGHTS = {'A': 131.2, 'C': 289.2, 'G': 329.2, 'T': 304.2}
"""dict of str or unicode to float: nucleotide molecular weights"""


def is_valid(nucleotides):
    """
    Is a given string a valid sequence of nucleotides? Does it
    only contain letters in the set a,A,c,C,g,G,t,T?

    :param nucleotides: nucleotides
    :type nucleotides: str or unicode
    :return: True if so, else False
    :rtype: bool
    """
    upper = nucleotides.upper()
    is_valid = True
    for c in upper:
        is_valid = is_valid and c in WEIGHTS
    return is_valid


def calculate_weight(sequence):
    """Calculate molecular weight of a DNA sequence.

    :param sequence: sequence
    :type sequence: str or unicode
    :return: molecular weight
    :rtype: float
    :raise AssertionError: if sequence is not valid
    """
    assert is_valid(sequence), \
        "Sequence should only contain A, C, G and T"
    weight = 0
    for c in sequence.upper():
        weight += WEIGHTS[c]
    return weight


if __name__ == "__main__":
    sequence = sys.argv[1]
    print(calculate_weight(sequence))
