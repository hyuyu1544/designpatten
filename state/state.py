"""State Pattern."""
from abc import ABCMeta, staticmethod


class Context(metaclass=ABCMeta):
    def __init__(self):
        pass

    def add_state(self):
        pass

    def change_state(self):
        pass

    def get_state(self):
        pass

    def _set_state_info(self):
        pass

    def _get_state_info(self):
        pass


class State:
    """state base."""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def is_match(self, state_info):
        pass

    @staticmethod
    def behavior(self):
        pass
