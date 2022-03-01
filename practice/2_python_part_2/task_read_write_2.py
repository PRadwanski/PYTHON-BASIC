"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words



# SOlution

def generate_words(*args):
    base_url = "/Users/pradwanski/Desktop/Python/tasks_2/file_{}.txt"
    i = 4
    with open(f, "w") as f:
        for arg in args:
            f.write(arg + "\n")

    i = 5
    with open(f"/Users/pradwanski/Desktop/Python/tasks_2/file_{i}.txt", "w") as f:
        for arg in args:
            f.write(arg + ",")

generate_words("Hakuna", "Matata", "Latam batam")
