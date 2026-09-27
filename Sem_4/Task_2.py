import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

ax1.set_xlim(-50, 50)
ax2.set_xlim(-50, 50)
ax3.set_xlim(-50, 50)
ax4.set_xlim(-50, 50)

v1 = np.random.normal(0, 10, 100)
v2 = np.random.normal(0, 10, 1000)
v3 = np.random.normal(0, 10, 10000)
v4 = np.random.normal(0, 10, 100000)

ax1.hist(v1, 100)
ax2.hist(v2, 100)
ax3.hist(v3, 100)
ax4.hist(v4, 100)

plt.show()