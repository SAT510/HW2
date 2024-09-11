import pytest

from hw2_debugging import merge_sort


def test_mergesort_random():
    A = [89, 67, 23, 12, 45, 100]
    B = [12, 23, 45, 67, 89, 100]
    assert (merge_sort(A)) == B


def test_mergesort_reverse():
    C = [100, 45, 23, 21, 20, 15, 9, 5, 2, 1]
    D = [1, 2, 5, 9, 15, 20, 21, 23, 45, 100]
    assert (merge_sort(C)) == D


def test_mergesort_negative():
    E = [-50, -90, -45, -9, -1, -43, -35, -76, -63]
    F = [-90, -76, -63, -50, -45, -43, -35, -9, -1]
    assert (merge_sort(E)) == F
