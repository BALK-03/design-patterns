from abc import ABC, abstractmethod
from builder.python.car import Car


class Builder(ABC):
    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_tires(self):
        pass

    @abstractmethod
    def set_color(self):
        pass

    @abstractmethod
    def build(self) -> Car:
        pass