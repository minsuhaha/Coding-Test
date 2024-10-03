def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    
    return ''.join(map(str, stack[:len(stack)-k]))