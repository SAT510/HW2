"""
This module handles generation of random numbers
"""

import secrets

def random_array(arr):
    """
    Replace each element in the array with a random number between 1 and 20.
    
    Args:
        arr (list): The input array to be filled with random numbers.
    
    Returns:
        list: The modified array with random numbers.
    """
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1
    return arr
