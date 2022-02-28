"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    ...

    
    
# Solution
def calculate_power_with_difference(arr):

    new_arr = []
    for i in range(0, len(arr)):
        if i == 0:
            new_arr.append(arr[i]**2)
        else:
            new_arr.append(arr[i]**2 - (arr[i-1]**2 - arr[i-1]))
    return new_arr

calculate_power_with_difference([1,2,3,4,5,6,7])
