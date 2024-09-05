import pytest 

from hw2_debugging import merge_sort

def test_mergesort_random_pass():
    A = [89, 67, 23, 12, 45, 100]
    B = [12, 23, 45, 67, 89, 100]
    assert(merge_sort(A)) == B

# def test_mergesort_fail():
    