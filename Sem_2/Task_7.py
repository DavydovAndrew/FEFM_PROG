nums = input().split()
r, k_m = 0, 0
for x in nums:
    k = nums.count(x)
    if k > k_m:
        r, k_m = x, k
print(r)