import math

radius = []
_start = 0
_range = 4
for _start in range(_range):
    radius.append(int(input("Place your radius value:" )))

def CalculateArea(radius):
    print(radius)
    output = []
    for _start in range(4):
        output.append(math.pi * (radius[_start] * radius[_start]))

    return output
    
print(CalculateArea(radius))
