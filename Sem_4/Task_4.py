import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('iris_data.csv')

fig, axes = plt.subplots(3, 2, figsize=(10, 6))
axes[0, 0].scatter(df['SepalLengthCm'], df['SepalWidthCm'], s=3)
axes[1, 0].scatter(df['SepalLengthCm'], df['PetalLengthCm'], s=3)
axes[2, 0].scatter(df['SepalLengthCm'], df['PetalWidthCm'], s=3)
axes[0, 1].scatter(df['PetalLengthCm'], df['PetalWidthCm'], s=3)
axes[1, 1].scatter(df['SepalWidthCm'], df['PetalWidthCm'], s=3)
axes[2, 1].scatter(df['PetalLengthCm'], df['SepalWidthCm'], s=3)

axes[0, 0].set_title('SepalWidth(SepalLength)')
axes[1, 0].set_title('PetalLength(SepalLength)')
axes[2, 0].set_title('PetalWidth(SepalLength)')
axes[0, 1].set_title('PetalWidth(PetalLength)')
axes[1, 1].set_title('PetalWidth(SepalWidth)')
axes[2, 1].set_title('SepalWidth(PetalLength)')

x1 = np.array([min(df['SepalLengthCm']), max(df['SepalLengthCm'])])
a1, b1 = np.polyfit(df['SepalLengthCm'], df['PetalLengthCm'], 1)
axes[1, 0].plot(x1, a1 * x1 + b1, 'r', label=f'a = {a1:.4f}, b = {b1:.4f}')
axes[1, 0].legend()

x2 = np.array([min(df['PetalLengthCm']), max(df['PetalLengthCm'])])
a2, b2 = np.polyfit(df['PetalLengthCm'], df['PetalWidthCm'], 1)
axes[0, 1].plot(x2, a2 * x2 + b2, 'r', label=f'a = {a2:.4f}, b = {b2:.4f}')
axes[0, 1].legend()

plt.tight_layout()
plt.show()