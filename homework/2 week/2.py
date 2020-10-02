mini = 10000
maxi = -10000
a = input().split()
for i in range(len(a)):
    if int(a[i]) < int(mini):
        mini = a[i]
        m1 = i
    if int(a[i]) > int(maxi):
        maxi = a[i]
        m2 = i
a[m1] = maxi
a[m2] = mini
print(" ".join(a))
