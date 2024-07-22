def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [0] # index 값을 담을 거임. (기본값으로 첫 numbers 찻 인덱스 값 넣어둠)
     
    for i in range(1, len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer
            
    
        