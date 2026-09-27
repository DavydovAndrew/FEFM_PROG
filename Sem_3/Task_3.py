def gcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = gcd(b, a % b)
    return y, x - y * (a // b), d

a, b = map(int, input().split())
print(' '.join(map(str, gcd(a, b))))