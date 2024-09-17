import sys
input = sys.stdin.readline

n = int(input())
nums = [1, 5, 10, 50]
cnt = set()

def dfs(res, length, idx):
    if length == n:
        cnt.add(res)
        return

    for i in range(idx, len(nums)):
        dfs(res+nums[i], length+1, i)

dfs(0, 0, 0)
print(len(cnt))
