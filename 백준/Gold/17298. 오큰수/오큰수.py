import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
answer = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)

print(*answer)
