n, s = input().split()
n = int(n)
for i in range(1, n // 2 + 1):
    print(i * s)
for i in range(n // 2 + (n % 2 != 0), 0, -1):
    print(i * s)