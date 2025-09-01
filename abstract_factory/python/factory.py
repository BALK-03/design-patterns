from abc import ABC, abstractmethod

from abstract_factory.python.fourniture import *

class FournitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

class ModernFournitureFactory(FournitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_sofa(self) -> Sofa:
        return ModernSofa()
    
class VectorianFournitureFactory(FournitureFactory):
    def create_chair(self):
        return VectorianChair()
    
    def create_sofa(self):
        return VectorianSofa()