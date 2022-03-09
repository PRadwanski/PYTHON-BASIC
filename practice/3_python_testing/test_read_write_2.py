def generate_words(*args):
    i = 4
    with open(f"/Users/pradwanski/Desktop/Python/tasks_2/file_{i}.txt", "w") as f:
        for arg in args:
            f.write(arg + "\n")

    i = 5
    with open(f"/Users/pradwanski/Desktop/Python/tasks_2/file_{i}.txt", "w") as f:
        for arg in args:
            f.write(arg + ",")
            

# tests
def test_write_files_1():

    with open("/Users/pradwanski/Desktop/Python/tasks_2/file_4.txt", "r") as f:
        content = f.read()
        f.close()
    assert content == 'Hakuna\nMatata\nLatam batam\n'

def test_write_files_2():

    with open("/Users/pradwanski/Desktop/Python/tasks_2/file_5.txt", "r") as f:
        content = f.read()  
        f.close()
    assert content == "Hakuna,Matata,Latam batam,"
