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


if __name__ == "__main__":

    school_timetable = Target()
    English_Teacher = EnglishTeacher()
    Math_Teacher = MathTeacher()
    school_timetable.add_observer(English_Teacher)
    school_timetable.add_observer(Math_Teacher)
    school_timetable.set_message('english class')
    school_timetable.set_message('math class')
