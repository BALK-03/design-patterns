class Car:
    def __init__(self):
        self.engine = None
        self.tires = None
        self.color = None

    def __str__(self):
        return f"Car: Engine={self.engine}, Tires={self.tires}, Color={self.color}"
