import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().rstrip()))
stack = []


for i in range(n):
    while stack and k > 0 and stack[-1] < nums[i]:
        stack.pop()
        k -= 1
    stack.append(nums[i])

print(''.join(map(str, stack[:len(stack)-k])))
