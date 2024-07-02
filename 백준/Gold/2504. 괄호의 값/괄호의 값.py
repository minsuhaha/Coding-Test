import sys
input = sys.stdin.readline

lst = input()
stack = []

res, tmp = 0, 1
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(lst[i])
        tmp *= 2
    elif lst[i] == '[':
        stack.append(lst[i])
        tmp *= 3
    elif lst[i] == ')':
        if stack:
            if stack[-1] == '(':
                stack.pop()
                if lst[i-1] == '(':
                    res += tmp
                tmp //= 2
            else:
                break
        else:
            stack.append(lst[i])
            break
    elif lst[i] == ']':
        if stack:
            if stack[-1] == '[':
                stack.pop()
                if lst[i-1] == '[':
                    res += tmp
                tmp //= 3
            else:
                break
        else:
            stack.append(lst[i])
            break

print(0 if stack else res)
