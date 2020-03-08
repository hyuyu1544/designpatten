"""Decorator Pattern."""
from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    """"""

    def __init__(self, input):
        self._input = input

    @abstractmethod
    def dosomething(self):
        pass


class ComponentImplA(Component):
    """"""

    def __init__(self, input):
        super.__init__(input)

    def dosomething(self):
        print("ComponentImplA dosomething.")


class ComponentImplB(Component):
    """"""

    def __init__(self, input):
        super.__init__(input)

    def dosomething(self):
        print('ComponentImplB dosomething.')


class Decorator(Component):
    """"""

    def __init__(self, Component):
        self._component = Component

    def dosomething(self):
        self._component.dosomething()
        self.behavior()

    @abstractmethod
    def behavior(self):
        pass


class DecoratorImplA(Decorator):
    """Decorator A."""

    def __init__(self, Component):
        super().__init__(Component)

    def behavior(self):
        print("DecoratorImplA behavior.")


class DecoratorImplB(Decorator):
    """Decorator B."""

    def __init__(self, Component):
        super().__init__(Component)

    def behavior(self):
        print("DecoratorImplB behavior.")
