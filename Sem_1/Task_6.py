with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
    nums = f_in.readline().split()
    oper = f_in.readline().strip()
    b = int(f_in.readline())
            
    for i in range(len(nums)):
        s_i = nums[i][::-1]
        n_i = 0
        for j in range(len(s_i)):
            n_i += int(s_i[j]) * b ** j
        nums[i] = n_i
    
    if oper == '+':
        k = sum(nums)
    elif oper == '-':
        k = 2 * nums[0] - sum(nums)
    else:
        k = 1
        for n in nums:
            k *= n

    sign = k < 0
    k = abs(k)
    s = ''
    digs = '0123456789abcdef'
    while k > 0:
        s += digs[k % b]
        k //= b
    f_out.write('-' * sign + s[::-1])