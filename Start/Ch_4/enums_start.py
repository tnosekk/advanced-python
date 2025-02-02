# Example file for Advanced Python: Language Features by Joe Marini
# define enumerations using the Enum base class
from enum import Enum, auto, unique

# TODO: enums have human-readable values and types


class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    RED_DELICIOUS = 1
    PEAR = auto()


# TODO: enums have name and value properties
# print(Fruit.APPLE)
# print(type(Fruit.APPLE))
# print(repr(Fruit.APPLE))

# print(Fruit.APPLE.name, Fruit.APPLE.value)
# TODO: print the auto-generated value
#print(Fruit.PEAR.value)
# TODO: enums are hashable - can be used as keys

my_fruits = {}
my_fruits[Fruit.BANANA] = "Come Mr. Tally man"
print(my_fruits[Fruit.BANANA])
