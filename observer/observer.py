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


class Work1(Observer):

    def update(self, observable, message):
        if observable.get_message() == 'work1':
            print('go throught Work1.')


class Work2(Observer):

    def update(self, observable, message):
        if observable.get_message() == 'work2':
            print('go throught Work2.')
