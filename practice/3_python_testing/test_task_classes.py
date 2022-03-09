# Exercise 1. Teacher, homework, student classes
class Teacher():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def create_homework(self, task_name, days_to_complete):
        return Homework(task_name, days_to_complete)


class Student(Teacher):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
    
    def do_homework(self, text, deadline):
        homework = Homework(text, deadline)
        if homework.is_active() == False:
            print("You are late")
        else:
            return homework
        

class Homework():
    ''' Everything should work fine, but I have a problem with date formats  '''
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.created = datetime.now() # Datetime.datetime

    def is_active(self):
        return timedelta(self.deadline) + self.created > datetime.now()


# Tests for classes

#teacher = Teacher('Dmitry', 'Orlyakov')
#student = Student('Vladislav', 'Popov')
#expired_homework = teacher.create_homework('Learn functions', 0)
#active_homework = teacher.create_homework("create 2 simple classes", 5)

# Fixtures

@pytest.fixture
def teacher():
    return Teacher('Dmitry', 'Orlyakov')

@pytest.fixture
def student():
    return Student('Vladislav', 'Popov')

# Tests
def test_teacher_1(teacher):
    assert teacher.first_name == "Dmitry" and teacher.last_name == "Orlyakov"

def test_teacher_2(teacher):
    expired_homework = teacher.create_homework('Learn functions', 0)
    assert expired_homework.is_active() == False

def test_teacher_3(teacher):
    active_homework = teacher.create_homework("create 2 simple classes", 5)
    assert active_homework.is_active() == True

def test_teacher_4(student):
    assert student.first_name == "Vladislav" and student.last_name == "Popov"
