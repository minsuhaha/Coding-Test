from collections import deque
def solution(s):
    s_lst = list(s)
    queue = deque(s_lst)
    
    cnt = 0
    for _ in range(len(s)):
        flag = True
        stack = []
        for i in range(len(s)):
            if queue[i] in '([{':
                stack.append(queue[i])
            elif queue[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack or stack[-1] in ['{', '[']:
                    flag = False
                    break
            elif queue[i] == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                elif not stack or stack[-1] in ['(', '[']:
                    flag = False
                    break
            elif queue[i] == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                elif not stack or stack[-1] in ['(', '{']:
                    flag = False
                    break
                    
        if flag and len(stack) == 0:
            cnt += 1
        queue.append(queue.popleft())
        
    return cnt