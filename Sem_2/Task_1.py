nums = list(map(int, input().split()))
print(sum(range(nums[0] + 1)) - sum(nums[1:]))