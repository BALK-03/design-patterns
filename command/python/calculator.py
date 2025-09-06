class Calculator:
    def __init__(self):
        self.curr = 0

    def add(self, val):
        self.curr += val
        print(f"Added {val}. Current value is {self.curr}")

    def subtract(self, val):
        self.curr -= val
        print(f"Subtracted {val}. Current value is {self.curr}")