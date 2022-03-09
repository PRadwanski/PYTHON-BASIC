# Exercise 2

def div_num(x, y):
    try:
        if y == 1:
            return x
        else:
            return x/y
    except ZeroDivisionError:
        return "Division by 0"
    

div_num(10, 0.3)


data = [
    (10,1,10),
    (8,2,4),
    (-2,2,-1),
    (-150, 5, -30)
]

@pytest.mark.parametrize("a,b,c", data)
def test_div_num(a,b,c):
    assert div_num(a,b) == c
