"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime


# Solution

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



if __name__ == '__main__':

    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'
    expired_homework.is_active()
    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00
    oop_homework.created
    oop_homework.is_active()

    student.do_homework(oop_homework.text, oop_homework.deadline)
    student.do_homework(expired_homework.text, oop_homework.deadline)  # You are late
