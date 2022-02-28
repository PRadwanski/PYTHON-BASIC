"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
from typing import List, Any


def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    ...

    
    
# Solution
def delete_from_list(arr, redundant):
    new_arr = []

    for item in arr:
        if item != redundant:
            new_arr.append(item)
    return new_arr

# With Pop method
def delete_from_list_2(arr, redundant):
    new_list = []

    while len(arr) > 0:
        poped_item = arr.pop(0)
        if poped_item != redundant:
            new_list.append(poped_item)
        else:
            del poped_item
        
    return new_list



my_list = [1,3,5,6,2,4,2,2,3,2]
my_list2 = [1,3,5,6,2,4,2,2,3,2]

delete_from_list(my_list, 2)
delete_from_list_2(my_list2, 2)
