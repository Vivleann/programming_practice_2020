def gcd(a , b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    t_gcd = a + b
    print(t_gcd)
    return t_gcd

print("Введите кол-во пар")
n = int(input())

print("Введите сами пары")

for i in range(n):
    a, b = input().split()
    gcd(int(a), int(b))
