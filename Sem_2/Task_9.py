with open('input.txt') as f:
    text = f.read()
flag = 1
k = 0
for ch in text:
    if ch in '.!?':
        k += flag
        flag = 0
    else:
        flag = 1
print(k)