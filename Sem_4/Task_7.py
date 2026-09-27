from string import punctuation as pnct

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()
lst = text.translate(str.maketrans(pnct, ' ' * len(pnct))).split()

words = {}
for elem in lst:
    if elem in words.keys():
        words[elem] += 1
    else:
        words[elem] = 1

freqs = sorted(words.items(), key=lambda elem: elem[1])
for i in range(1, 11):
    print(freqs[-i][0], freqs[-i][1])