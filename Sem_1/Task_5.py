n = input()[::-1]
b = int(input())
c = int(input())
k = 0
for i in range(len(n)):
    k += int(n[i]) * b ** i

s = ''
while k > 0:
    s += str(k % c)
    k //= c
print(s[::-1])