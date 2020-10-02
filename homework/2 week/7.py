n = int(input())
s = set()
for i in range(n):
    x = set(input().split())
    s = s | x
    
print(len(s))
