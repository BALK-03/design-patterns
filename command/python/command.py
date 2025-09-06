from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class AddCommand(Command):
    def __init__(self, calculator, value):
        self.calculator = calculator
        self.value = value

    def execute(self):
        self.calculator.add(self.value)
    
    def undo(self):
        self.calculator.subtract(self.value)

class SubtractCommand(Command):
    def __init__(self, calculator, value):
        self._calculator = calculator
        self._value = value

    def execute(self):
        self._calculator.subtract(self._value)

    def undo(self):
        self._calculator.add(self._value)