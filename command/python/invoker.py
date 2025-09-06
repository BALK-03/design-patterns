class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            print("Undoing last command...")
            command.undo()
        else:
            print("Nothing to undo.")