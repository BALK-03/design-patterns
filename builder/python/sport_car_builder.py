from builder.python.builder import Builder
from builder.python.car import Car


class SportsCarBuilder(Builder):
    def __init__(self):
        self.product = Car()

    def set_engine(self):
        self.product.engine = "V8 Turbo"

    def set_tires(self):
        self.product.tires = "Performance Tires"

    def set_color(self):
        self.product.color = "Red"

    def build(self) -> Car:
        return self.product
    

class SUVBuilder(Builder):
    def __init__(self):
        self.product = Car()

    def set_engine(self):
        self.product.engine = "V6"

    def set_tires(self):
        self.product.tires = "All-terrain Tires"

    def set_color(self):
        self.product.color = "Black"

    def get_result(self) -> Car:
        return self.product