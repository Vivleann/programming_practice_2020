import numpy as np

class Vector():
    def __init__(self, *args):
    
        if len(args)==0:
            self.values = (0,0)
        else:
            self.values = args

    def norma(self):
        return sum( num**2 for num in self.values) ** 0.5

    def multiply_on_number(self, a):
        
        return(tuple(num * a for num in self.values))

    def add(self, other):
        return tuple(a+b for a, b in zip(self.values, other.values))

    def sub(self, other):
        return tuple(a-b for a, b in zip(self.values, other.values))
    
    def div(self, other):
        return tuple(a/b for a, b in zip(self.values, other.values))

    def scalor_multiply(self, other):
        return sum(a*b for a, b in zip(self.values, other.values))
    
    def vector_multiply(self, other):
        return np.cross(self.values, other.values)
    
    def dimension(self):
        return len(self.values)
    
    def is_collinearity(self, other):
        if (len(set(tuple(a/b for a, b in zip(self.values, other.values))))) == 1:
            return 1
        else:
            return 0
        
k = Vector(1, 2)
d = Vector(6, 4)

print("Взятие нормы вектора")
print(k.norma())
print("Умножение на число")
print(k.multiply_on_number(5))
print("Сложение")
print(k.add(d))
print("Вычитание")
print(k.sub(d))
print("Деление")
print(k.div(d))
print("Скалярное умножение")
print(k.scalor_multiply(d))
print("Векторное умножение")
print(k.vector_multiply(d))
print("Размерность")
print(k.dimension())
print("Проверка на коллинеарность")
print(k.is_collinearity(d))
