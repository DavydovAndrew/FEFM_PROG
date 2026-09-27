import numpy as np

def slu(A, b):
    return np.linalg.lstsq(A, b, rcond=None)[0]

n, m = map(int, input().split())
A, b = [], []
for _ in range(n):
    s = list(map(int, input().split()))
    A.append(s[:-1])
    b.append([s[-1]])
    
print(slu(np.array(A), np.array(b)))