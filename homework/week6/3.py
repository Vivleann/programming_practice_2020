import math

def sq_triangle(a, b ):
    S = a * b / 2

    print(S)
    return S
def circle(r):
    S = 3.14 * r * r

    print(S)
    return S

def rectangle(a, b):
    S = a * b
    print(S)
    return S

print("Введите 1 - треугольник 2 - круг 3 - прямоугольник ")

k = int(input())
if k == 1:
    print("Введите длину первой и второй стороны")
    a = int(input())
    b = int(input())

    sq_triangle(a, b )

if k == 2:
    print("Радиус")
    r = int(input())
    circle(r)

if k == 3:
    print("1 и 2 стороны")
    a = int(input())
    b = int(input())
    rectangle(a, b)
        
