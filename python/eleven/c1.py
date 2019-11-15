from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1

print(VIP.YELLOW)
print(VIP.GREEN.value)
print(VIP.GREEN.name)

for v in VIP:
    print(v)