from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    queue = deque(people)
    cnt = 0
    while queue:
        p = queue.popleft() # 가장 큰 값 빼주기
        max_people = 1 # 최대 2명까지 가능
        total = p
        while queue and max_people==1:
            if total+queue[-1] > limit:
                break
            queue.pop()
            max_people += 1
        cnt += 1
    return cnt
            
             