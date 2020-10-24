def det(diag):
    
    print( sum(diag))
    return sum(diag)

k = int(input())
l = []
r = []
for i in range(k):
    s = input().split()
    
    l.append(int(s[i]))
    num = len(s) - i - 1
    r.append(int(s[num]))
print("Введите 1 для главной и 2 для побочной")
i = int(input())
if i == 1:
    det(l)
if i == 2:
    det(r)
