import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p_func = input().rstrip()
    n = int(input())
    lst = input().rstrip()[1:-1].split(',')

    if n:
        queue = deque(lst)
    else:
        queue = deque([])
    
    R_cnt = 0   
    for p in p_func:
        if p == 'R':
            R_cnt += 1
        elif p == 'D':
            if queue:
                if R_cnt % 2 != 0:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                R_cnt = -1 # error 처리
                break

    if R_cnt == -1:
        print('error')
    else:
        if R_cnt % 2 != 0:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
