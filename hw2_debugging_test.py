"""
Performstesting of merge sort
"""

from hw2_debugging import merge_sort


def test_mergesort_random():
    """
    Test 1 for mergesort
    """
    a = [89, 67, 23, 12, 45, 100]
    b = [12, 23, 45, 67, 89, 100]
    result = merge_sort(b)
    if result != b:
        raise ValueError(f"Expected {b}, but got {result}")


def test_mergesort_reverse():
    """
    Test 2 for mergesort
    """
    c = [100, 45, 23, 21, 20, 15, 9, 5, 2, 1]
    d = [1, 2, 5, 9, 15, 20, 21, 23, 45, 100]
    result = merge_sort(d)
    if result != d:
        raise ValueError(f"Expected {d}, but got {result}")



def test_mergesort_negative():
    """
    Test 3 for mergesort
    """
    e = [-50, -90, -45, -9, -1, -43, -35, -76, -63]
    f = [-90, -76, -63, -50, -45, -43, -35, -9, -1]
    result = merge_sort(e)
    if result != f:
        raise ValueError(f"Expected {f}, but got {result}")
