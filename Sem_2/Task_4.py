s = input().split()
s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
print(' '.join(s))