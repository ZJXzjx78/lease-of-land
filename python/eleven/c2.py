from enum import Enum

class VIP(Enum):
    YELLOW = 1
    YELLOW1 = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1

# result = VIP.GREEN == VIP.BLACK
# result = VIP.GREEN is VIP.GREEN
# print(result)

for v in VIP._missing_():
    print(v)