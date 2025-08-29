from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def business_logic(self):
        pass


class ModernChair(Chair):
    def business_logic(self):
        print("This is a Modern Chair!")


class VectorianChair(Chair):
    def business_logic(self):
        print("This is a Vectorian Chair!")


class Sofa(ABC):
    @abstractmethod
    def business_logic(self):
        pass


class ModernSofa(Sofa):
    def business_logic(self):
        print("This is a Modern Sofa!")


class VectorianSofa(Sofa):
    def business_logic(self):
        print("This is a Vectorian Sofa!")