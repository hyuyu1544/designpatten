"""Strategy Pattern."""
from abc import ABCMeta, abstractclassmethod


class Context:
    """Execute strategy from client."""

    def __init__(self, strategy):
        self._strategy = strategy

    def strategy_execute(self):
        self._strategy.execute()


class Strategy(metaclass=ABCMeta):
    """Strategy Interface."""

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @abstractclassmethod
    def execute(self):
        """Implement different strategy."""
        pass
