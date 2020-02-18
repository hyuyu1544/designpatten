"""State Pattern."""
from abc import ABCMeta, staticmethod


class Context(metaclass=ABCMeta):
    def __init__(self):
        self.__states = []
        self.__current_states = None
        self.__state_info = 0

    def add_state(self, state):
        if state not in self.__states:
            self.__state.append(state)

    def change_state(self, state):
        if state is None:
            return False
        if self.__current_states is None:
            print('initial state: {}'.format(state))
        else:
            print('{} state turn to {} state.'.format(
                self.__current_states, state))
        self.__current_states = state
        self.add_state(state)
        return True

    def get_state(self):
        return self.__current_states

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)

    def _get_state_info(self):
        return self.__state_info


class State:
    """state base."""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def is_match(self, state_info):
        return False

    @staticmethod
    def behavior(self):
        pass
