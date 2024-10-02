'''
문제
-  Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
-  A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
-  A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1
'''

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
ans = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and num[stack[-1]] < num[i]:
        ans[stack.pop()] = num[i]
    stack.append(i)

print(*ans)
