from command.python.calculator import Calculator
from command.python.invoker import Invoker
from command.python.command import AddCommand, SubtractCommand


calculator = Calculator()
invoker = Invoker()

invoker.execute_command(AddCommand(calculator, 10))
invoker.execute_command(AddCommand(calculator, 5))
invoker.execute_command(SubtractCommand(calculator, 2))

print("\n--- Performing undos ---")
invoker.undo_last_command()
invoker.undo_last_command()
invoker.undo_last_command()
invoker.undo_last_command()