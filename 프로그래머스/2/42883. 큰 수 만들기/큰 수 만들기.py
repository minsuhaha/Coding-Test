def solution(number, k):
    stack = []
    for n in number:
        while stack and k > 0:
            if stack[-1] < n:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(n)
    return ''.join(stack[:len(stack)-k])
                
        