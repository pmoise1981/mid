from abc import ABC, abstractmethod
from calculator import Calculator
from history_manager import HistoryManager

class Command(ABC):
    """Abstract base class for commands."""
    
    @abstractmethod
    def execute(self):
        pass

class AddCommand(Command):
    def __init__(self, calculator: Calculator, x, y):
        self.calculator = calculator
        self.x = x
        self.y = y

    def execute(self):
        return self.calculator.add(self.x, self.y)

class SubtractCommand(Command):
    def __init__(self, calculator: Calculator, x, y):
        self.calculator = calculator
        self.x = x
        self.y = y

    def execute(self):
        return self.calculator.subtract(self.x, self.y)

class MultiplyCommand(Command):
    def __init__(self, calculator: Calculator, x, y):
        self.calculator = calculator
        self.x = x
        self.y = y

    def execute(self):
        return self.calculator.multiply(self.x, self.y)

class DivideCommand(Command):
    def __init__(self, calculator: Calculator, x, y):
        self.calculator = calculator
        self.x = x
        self.y = y

    def execute(self):
        return self.calculator.divide(self.x, self.y)

class HistoryCommand(Command):
    def __init__(self, history_manager: HistoryManager):
        self.history_manager = history_manager

    def execute(self):
        return self.history_manager.load_history()

class ClearHistoryCommand(Command):
    def __init__(self, history_manager: HistoryManager):
        self.history_manager = history_manager

    def execute(self):
        self.history_manager.clear_history()
        return "Calculation history cleared."

class CommandInvoker:
    """Invoker class to execute commands."""
    
    def __init__(self):
        self.history = []
    
    def execute_command(self, command: Command):
        result = command.execute()
        self.history.append(command)
        return result

