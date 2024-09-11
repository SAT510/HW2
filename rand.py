"""
This module handles generation of random numbers
"""

import secrets


def random_array(arr):
    """
    Replace a given array element with a random integer falling between 1 and 20.

    Args:
        arr (list): The list where we are filling with random integers between 1 and 20.

    Returns:
        list: The new array with integers (random) between 1 and 20.
    """
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1



    return arr
