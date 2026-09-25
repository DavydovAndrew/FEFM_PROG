g, s = input().split()
g = int(g) # Судя по тестам, g - длина группы, а не число групп
r = ''
for i in range(0, len(s), g):
    r += s[i:i + g][::-1]
print(r)