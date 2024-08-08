def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            if s[i] == ')':
                return False
        if s[i] == '(':
            stack.append('(')
        else:
            stack.pop()
    
    return True if not stack else False
            
            
    
        