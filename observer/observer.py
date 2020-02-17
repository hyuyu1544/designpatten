"""Observer Pattern."""
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, observable, message):
        pass


class Observable:

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self, message='TEST'):
        for obj in self.observers:
            obj.update(self, message)


class Target(Observable):

    def __init__(self):
        super().__init__()
        self._message = ''

    def get_message(self):
        return self._message

    def set_message(self, input_message):
        self._message = input_message
        self.notify_observer(self._message)


class EnglishTeacher(Observer):

    def update(self, observable, message):
        if observable.get_message() == 'english class':
            print("Let's start english class.")


class MathTeacher(Observer):

    def update(self, observable, message):
        if observable.get_message() == 'math class':
            print("Let's start math class.")


if __name__ == "__main__":
    """An example.

    Two teachers, one is english teacher and another is math teacher.
    Both of them what to know when should teach the class.
    If school timetable show is `english class`, english teacher will teach the class.
    If school timetable show is `math class`, math teacher will teach the class. 
    """
    school_timetable = Target()
    English_Teacher = EnglishTeacher()
    Math_Teacher = MathTeacher()
    school_timetable.add_observer(English_Teacher)
    school_timetable.add_observer(Math_Teacher)
    school_timetable.set_message('english class')
    school_timetable.set_message('math class')
