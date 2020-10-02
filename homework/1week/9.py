import math
def distance(x1, y1, x2, y2):
    dis = abs(x2 - x1)**2 + abs(y2 - y1)**2
    return math.sqrt(dis)
    
print(distance(float(input()), float(input()), float(input()), float(input())))
