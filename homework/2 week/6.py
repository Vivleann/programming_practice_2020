a = input().split()
for i in  range(len(a)):
    if a[i] in a[0:i]:
        print("YES")
    else:
        print("NO")
