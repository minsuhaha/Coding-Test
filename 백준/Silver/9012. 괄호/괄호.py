import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    vps = input().rstrip()
    stack = []

    for v in vps:
        if v == '(':
            stack.append(v)
        else:
            if not stack:
                stack.append(v)
                break
            stack.pop()

    if stack:
        print('NO')
    else:
        print('YES')
