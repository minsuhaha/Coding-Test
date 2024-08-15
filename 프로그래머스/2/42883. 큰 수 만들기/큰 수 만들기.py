def solution(number, k):
    stack = []
    n = len(number)

    for i in range(len(number)):
        while stack and len(stack)+n-(i+1) >= n-k and stack[-1] < number[i]:
            stack.pop()
        stack.append(number[i])
    
    if len(stack) > n-k:
        return ''.join(stack[:(n-k)])
    return ''.join(stack)