"""
dna.sequence tests.
"""
import numpy as np
import pytest
from sequence import calculate_weight
from sequence import WEIGHTS


def test_calculate_weight():
    """
    Use numpy.isclose function to check that a molecular weight for G
    returned from sequence.calculate_weight() is the same as the
    weight recorded for G in the WEIGHTS dictionary.
    np.isclose compares two values to within a given tolerance or
    delta (atol) here, 0.01.
    If np.isclose is False then the assert fails, an
    AssertionError is raised and the test fails.
    """
    assert np.isclose(WEIGHTS['G'],
                      calculate_weight("G"),
                      atol=0.01), \
                      "Weight returned was unexpected"


def test_gatttacca():
    """
    Similar to test_calculate_weight but with a multi-character sequence.
    """
    sequence = "GATTACCA"
    weight = calculate_weight(sequence)
    assert np.isclose(1909.6, weight, atol=0.01), \
        "Weight returned was unexpected"


def test_empty_sequence():
    """
    Similar to test_calculate_weight but with an empty sequence.
    """
    sequence = ""
    assert np.isclose(0, calculate_weight(sequence), atol=0.0), \
        "Weight returned was unexpected"



def test_calculate_weight_invalid_sequence():
    """
    Test that calculate_weight raises an AssertionError if given a
    string of invalid (non-G,A,T,C) characters.
    """
    with pytest.raises(AssertionError):
        _ = calculate_weight("ACGTX")
