a = input().split()
d = {}
count = 0
for item in a:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
for key, value in d.items():
    count += value * (value - 1)
print(count/2)
