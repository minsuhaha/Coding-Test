import sys
input = sys.stdin.readline

nums = input().rstrip().split('-')
res = 0
for i in range(len(nums)):
    if i == 0:
        if '+' in nums[i]:
            n_num = map(int, nums[i].split('+'))
            res += sum(n_num)
        else:
            res += int(nums[i])
    else:
        if '+' in nums[i]:
            n_num = map(int, nums[i].split('+'))
            res -= sum(n_num)
        else:
            res -= int(nums[i])

print(res)
