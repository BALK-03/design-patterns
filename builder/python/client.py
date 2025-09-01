from builder.python.director import Director
from builder.python.sport_car_builder import SportsCarBuilder


dir = Director()

sports_car_builder = SportsCarBuilder()
dir.construct_car(
    builder=sports_car_builder,
)
sports_car = sports_car_builder.build()

print(sports_car)