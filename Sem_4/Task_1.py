import matplotlib.pyplot as plt
import numpy as np

n = [1, 3, 5, 7, 9, 2, 4, 6, 8]
y_1 = [124.8, 375, 641, 892, 1148, 256, 511, 767, 1030]
y_2 = [156, 469, 784, 1100, 1435, 313, 627, 941, 1256]
y_3 = [180.8, 547, 911, 1281, 1648, 362, 731, 1090, 1465]
y_4 = [201.9, 608, 1018, 1432, 1840, 405, 810, 1217, 1626]

fig_1 = plt.figure(figsize=(6, 8))
ax_1 = fig_1.add_subplot(111)
ax_1.scatter(n, y_1, color='b', label='T = 9.226')
ax_1.scatter(n, y_2, color='r', marker='x', label='T = 14.052')
ax_1.scatter(n, y_3, color='y', marker='s', label='T = 18.873')
ax_1.scatter(n, y_4, color='m', marker='^', label='T = 23.655')

x = np.array([1, 9])
u_1, b_1 = np.polyfit(n, y_1, 1)
ax_1.plot(x, u_1 * x + b_1, 'b')
u_2, b_2 = np.polyfit(n, y_2, 1)
ax_1.plot(x, u_2 * x + b_2, 'r')
u_3, b_3 = np.polyfit(n, y_3, 1)
ax_1.plot(x, u_3 * x + b_3, 'y')
u_4, b_4 = np.polyfit(n, y_4, 1)
ax_1.plot(x, u_4 * x + b_4, 'm')

ax_1.set_xlabel('n')
ax_1.set_ylabel('Частота n-ой гармоники, Гц')
ax_1.legend()
fig_1.tight_layout()
fig_1.savefig('Freq(n).png', dpi=300)
# plt.show()


fig_2 = plt.figure(figsize=(6, 6))
ax_2 = fig_2.add_subplot(111)
U = np.array([u_1, u_2, u_3, u_4]) ** 2
T = np.array([9.226, 14.052, 18.873, 23.655])
r, c = np.polyfit(T, U, 1)
ax_2.scatter(T, U)
ax_2.plot(T, r * T + c)

ax_2.set_xlabel('T, Н')
ax_2.set_ylabel('$u^2$, $(м/с)^2$')
fig_2.tight_layout()
fig_2.savefig('U2(T).png', dpi=300)
# plt.show()

print(f'U = {u_1, u_2, u_3, u_4}')
print(f'Rho = {1 / r}')


fig_3 = plt.figure(figsize=(6, 6))
ax_3 = fig_3.add_subplot(111)
freqs = [175, 175, 178, 179, 179.8, 180.1, 180.2, 180.3,
         180.4, 180.5, 180.6, 180.7, 180.9, 181.2,
         181.3, 181.45, 181.5, 181.51, 181.6, 181.7, 181.8,
         181.9, 182.3, 182.9, 183.7, 184.5]
ampls = np.array([0.1, 0.2, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
         1.1, 1.3, 3, 5, 3.2, 1.8, 1.3, 1, 0.9, 0.8, 0.7,
         0.6, 0.4, 0.3, 0.2, 0.2])
ax_3.plot(freqs, ampls / max(ampls))

ax_3.set_xlabel('Частота, Гц')
ax_3.set_ylabel('Амплитуда, доля от max')
ax_3.grid()
fig_3.tight_layout()
fig_3.savefig('АЧХ.png', dpi=300)
# plt.show()