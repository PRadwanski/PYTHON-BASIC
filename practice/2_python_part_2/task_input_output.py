"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    ...

    
# Solution

def read_numbers(enters, n):
    output = 0
    counter = 0
    for i in range(n-1):
        if type(enters[i]) == int or type(enters[i]) == float:
            output += enters[i]
            counter += 1

    if output == 0:
        return "No numbers entered"

    return f"Avg: {round(output/counter, 2)}"


read_numbers(["Bunny", "Dog", 5, 6, 10], 5)

