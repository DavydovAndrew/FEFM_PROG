import numpy as np
from random import gauss

def gen_data(N, a, b):
    x = np.random.randint(1, 100, N)
    y = a * x + b
    for i in range(N):
        y[i] = gauss(y[i], 2)
    return x, y