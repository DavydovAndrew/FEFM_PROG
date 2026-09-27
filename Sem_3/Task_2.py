def factor(n, x = 2):
    while x * x <= n: 
        if n % x:
            x += 1
        else:
            return [x] + factor(n // x, x)
    return [n]
        
print(factor(int(input())))