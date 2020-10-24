import matplotlib.pyplot as plt

xa = []

def first(x):
    y = 2 *x
    return(y)

def second(x):
    y = x * x
    return(y)

def third(x):
    y = 2* abs(x) -1
    return(y)
    

x = int(input())
ya = []
if x > 5:
    print(first(x))
elif x < -5:
    print(third(x))
    
else:
    print(second(x))

for x in range(-10, 11):
    xa.append(x)
    if x > 5:
        ya.append(first(x))
    elif x < -5:
        ya.append(third(x))
    else:
        ya.append(second(x))
plt.plot(xa,ya)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()
print(xa)
print(ya)
