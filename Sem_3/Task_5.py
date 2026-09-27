import numpy as np

def spiral(n, m):
    l, r, t, b = 0, m, 0, n
    out = np.zeros((n, m))
    x = 1
    while l < r and t < b:
        out[t, l:r] = np.arange(x, x + r - l)
        t += 1
        x += r - l

        if t < b:
            out[t:b, r - 1] = np.arange(x, x + b - t)
            r -= 1
            x += b - t
        else:
            break

        if l < r:
            out[b - 1, l:r][::-1] = np.arange(x, x + r - l)
            b -= 1
            x += r - l
        else:
            break

        if t < b:
            out[t:b, l][::-1] = np.arange(x, x + b - t)
            l += 1
            x += b - t
        else:
            break
    return out

n, m = map(int, input().split())
A = spiral(n, m)
for i in range(n):
    print(i * A[i])