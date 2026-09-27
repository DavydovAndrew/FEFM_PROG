import numpy as np

def mnk(x, y): # x, y - arrays
    a, b = np.polyfit(x, y, 1)
    return f'a = {a}, b = {b}'