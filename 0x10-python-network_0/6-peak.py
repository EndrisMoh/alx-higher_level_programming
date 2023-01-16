#!/usr/bin/python3
"""Technical interview preparation: a function that finds a peak in
    a list of unsorted integers
"""

"""
    Algorithm Complexity Process
        it is not sorted, so sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)
        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""


def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_int = None
    for n in list_of_integers:
        if max_int is None or max_int < n:
            max_int = n
    return max_int
