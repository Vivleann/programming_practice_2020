n = int(input())
prev = 1
count = 0
for i in range(1, n + 1):
    prev *=  i
    count += prev
print(count)
