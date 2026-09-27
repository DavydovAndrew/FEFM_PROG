import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')
counts = df['Species'].value_counts()
plt.pie(counts, labels=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
plt.show()

x_1 = sum(df['PetalLengthCm'] <= 1.2)
x_2 = sum((df['PetalLengthCm'] > 1.2) & (df['PetalLengthCm'] <= 1.5))
x_3 = sum(df['PetalLengthCm'] > 1.5)
plt.pie((x_1, x_2, x_3), labels=['Short', 'Medium', 'Long'])
plt.show()