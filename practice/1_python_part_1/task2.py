"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
from typing import Dict


def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict:
    ...

    
# Solution

my_dict = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":4}
second_dict = {"a":5, "b":5, "c":5, "d":3, "e":3}


def set_to_dict(dictionary, updates):
    for key, value in updates.items():
        if updates[key] > dictionary[key]:
            dictionary[key] = value
    return dictionary


set_to_dict(my_dict, second_dict)
