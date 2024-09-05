from collections import deque
def solution(priorities, location):
    queue = deque((idx, num) for idx, num in enumerate(priorities))
    answer = []
    
    # while queue:
    #     idx, num = queue.popleft()
    #     flag = True
    #     for idx2, num2 in queue:
    #         if num < num2:
    #             queue.append((idx, num))
    #             flag = False
    #             break
    #     if flag:
    #         answer.append(idx)
    
    while queue:
        idx, num = queue.popleft()
        
        if any(num < num2 for idx2, num2 in queue):
            queue.append((idx, num))
        else:
            answer.append(idx)
            
    return answer.index(location)+1
        
        
            
        