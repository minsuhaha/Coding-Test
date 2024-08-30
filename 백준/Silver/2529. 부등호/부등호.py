import sys
input = sys.stdin.readline

k = int(input())
signs = list(input().rstrip().split())
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def dfs(res, idx):
    if idx == k:
        ans.append(''.join(map(str, res)))
        return

    for num in nums:
        if num not in res:
            if signs[idx] == '<' and res[-1] < num:
                res.append(num)
                dfs(res, idx+1)
                res.pop()
            elif signs[idx] == '>' and res[-1] > num:
                res.append(num)
                dfs(res, idx+1)
                res.pop()

ans = []
for num in nums:
    res = [num]
    dfs(res, 0)

print(ans[-1])
print(ans[0])
