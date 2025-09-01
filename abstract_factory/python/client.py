from abstract_factory.python.factory import ModernFournitureFactory, VectorianFournitureFactory
from abstract_factory.python.fourniture import Chair, Sofa


# Modern Factory
modern_factory = ModernFournitureFactory()
modern_chair: Chair = modern_factory.create_chair()
modern_chair.business_logic()

modern_sofa: Sofa = modern_factory.create_sofa()
modern_sofa.business_logic()

# Vectorian Factory
vectorian_factory = VectorianFournitureFactory()
vectorian_chair: Chair = vectorian_factory.create_chair()
vectorian_chair.business_logic()

vectorian_sofa: Sofa = vectorian_factory.create_sofa()
vectorian_sofa.business_logic()