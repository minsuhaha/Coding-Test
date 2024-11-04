from collections import deque
def solution(priorities, location):
    process = deque()
    for idx, value in enumerate(priorities):
        process.append((idx, value))
    
    seq = 0
    while process:
        idx, proc = process.popleft()
        flag = True
        for i, p in process:
            if proc < p:
                flag = False
                break
        if flag:
            seq += 1
            if location == idx:
                return seq
        else:
            process.append((idx, proc))
        
        