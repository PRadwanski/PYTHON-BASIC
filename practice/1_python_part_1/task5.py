"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    ...

    
    
# Solution

my_sentence = "Hi hi 1 1 I am a new guy here. 3 3 4 4 5"

def remove_duplicated_words(sentence):
    new_set = set(sentence.split())
    return " ".join(new_set)

remove_duplicated_words(my_sentence)
