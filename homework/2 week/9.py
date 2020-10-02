res = []
n = int(input())
d = {}
num = 0
for i in range(n):
    s = input().split()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
for key in d:
    if d[key] > num:
        num = d[key]
        res = []
        res.append(key)
    elif d[key] == num:
        res.append(key)
print(sorted(res)[0])
        
        

 
      
            
        



