from collections import deque
def solution(people, limit):
    people.sort()
    
    cnt = 0
    L, R = 0, len(people)-1
    while L <= R:
        if people[L] + people[R] <= limit:
            L += 1
            R -= 1
        else:
            R -= 1
        cnt += 1
    return cnt
        
        
    