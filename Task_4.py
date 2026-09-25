with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
    nums = list(map(int, f_in.readline().split()))
    oper = f_in.readline().strip()
    if oper == '+':
        f_out.write(str(sum(nums)))
    elif oper == '-':
        f_out.write(str(2 * nums[0] - sum(nums)))
    else:
        pr = 1
        for n in nums:
            pr *= n
        f_out.write(str(pr))