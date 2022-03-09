# Exercise 3

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


# tests
data = [
    (["Bunny", "Dog", 5, 6, 10], 5,'Avg: 5.5'),
    (['Fasolka', "Szkic", "Duzo"], 1, "No numbers entered"),
    ([1,2,3,4],2,'Avg: 1.0')
]

@pytest.mark.parametrize("a,b,c",data)
def test_read_numbers(a,b,c):
    assert read_numbers(a,b) == c
