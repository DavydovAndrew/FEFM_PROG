nums = list(map(int, input().split()))
prod = 1
for n in nums:
    prod *= n
print(prod ** (1 / len(nums)))