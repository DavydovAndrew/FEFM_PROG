import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('BTC_data.csv')
n = len(df['time'])

x_ls = np.array([0])
for i in range(0, n, n // 25):
    s = df['time'][i]
    date = s[:s.find('T')].split('-')
    x_ls = np.append(x_ls, f'{date[2]}-{date[1]}-{date[0]}')

x = np.arange(1, n + 1)
y = np.array([0])
p = np.poly1d(np.polyfit(x, df['close'], 11))
for i in x:
    y = np.append(y, p(i))

plt.figure(figsize=(16, 8))
plt.plot(x, df['close'], label='Реальность')
plt.plot(x, y[1:], 'r', label='Подгон 11-ой степенью')

plt.xticks(x[::n // 25], labels=x_ls[1:], rotation=90)
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.legend()

plt.tight_layout()
plt.show()