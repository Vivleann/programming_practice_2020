
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

    def scalor_multiply(self, other):
        return sum(a*b for a, b in zip(self.values, other.values))
    
    
    def dimension(self):
        return len(self.values)
    
    def collinearity(self, other):
        print(len(set(tuple(a/b for a, b in zip(self.values, other.values)))))
        
k = Vector(1, 2)
d = Vector(2, 4)
print(k.collinearity(d))
