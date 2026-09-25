with open('input.txt', 'r', encoding='utf-8') as f:
    text = ' ' + f.read()
flag = True
i = 0
while i < len(text):
    if text[i] in 'ёуеыаоэяию':
        if flag:
            text = text[:i + 1] + 'с' + text[i] + text[i + 1:]
            flag = False
            i += 2
    else:
        flag = True
    i += 1
print(text.strip())