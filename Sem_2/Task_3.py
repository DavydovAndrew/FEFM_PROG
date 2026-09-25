s = input()

def is_mir(s):
    lets = 'EJSZ3L25'
    k = 0
    for i in range(len(s)):
        a, b = s[i], s[::-1][i]
        k += a in 'AHIMOTUVWXY18' and a == b
        for j in range(4):
            k += (a == lets[j] and b == lets[j + 4]) or (b == lets[j] and a == lets[j + 4])
    return k == len(s)

if s == s[::-1] and is_mir(s):
    print(f'"{s} is a mirrored palindrome."')
elif s == s[::-1]:
    print(f'"{s} is a regular palindrome."')
elif is_mir(s):
    print(f'"{s} is a mirrored string."')
else:
    print(f'"{s} is not a palindrome."')