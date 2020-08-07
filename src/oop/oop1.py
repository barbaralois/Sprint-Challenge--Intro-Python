# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class is Vehicle
class Vehicle:
    pass

# These two inherit from Vehicle
class GroundVehicle(Vehicle):
    pass

class FlightVehicle(Vehicle):
    pass

# These two inherit from GroundVehicle
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

# These two inherit from FlightVehicle
class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass