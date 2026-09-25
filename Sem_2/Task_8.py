n = int(input())
nums = list(map(int, input().split()))
for i in nums:
    k = 0
    for j in nums:
        k += j < i
    if k == n // 2:
        print(i)
        break