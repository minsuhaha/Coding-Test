from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    
    cnt, max_cnt = 0, len(queue1)*3
    
    while sum1 != sum2:
        if cnt == max_cnt:
            return -1
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = q2.popleft()
            q1.append(num)
            sum2 -= num
            sum1 += num
        cnt += 1
    return cnt
        
    
