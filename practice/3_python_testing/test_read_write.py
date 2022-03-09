def reading_files():
    result = ""
    for i in range(1, 4):
        with open(f"/Users/pradwanski/Desktop/Python/tasks_2/file_{i}.txt") as f:
            result = result + f.read() + " "
            f.close()
    return result

# Tests

def test_reading_files():
    assert reading_files() == "23 78 3 "
