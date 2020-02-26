"""Take school class schedule for example."""
from observer import Observer, Observable


class SchoolSchedule(Observable):
    """Create a target."""

    def __init__(self):
        super().__init__()
        self.message = ''

    def set_message(self, input_message):
        self.message = input_message
        self.notify_observer(self.message)

    def get_message(self):
        return self.message


class EnglishTeacher(Observer):
    def update(self, observable, message):
        if observable.get_message() == 'english class':
            print("Let's start english class.")


class MathTeacher(Observer):
    def update(self, observable, message):
        if observable.get_message() == 'math class':
            print("Let's start math class.")


"""An example.

Two teachers, one is english teacher and another is math teacher.
Both of them what to know when should teach the class.
If school timetable show is `english class`, english teacher will teach the class.
If school timetable show is `math class`, math teacher will teach the class. 
"""
school_timetable = SchoolSchedule()
englishteacher = EnglishTeacher()
mathteacher = MathTeacher()
school_timetable.add_observer(englishteacher)
school_timetable.add_observer(mathteacher)
school_timetable.set_message('english class')
school_timetable.set_message('math class')
