import sys
from collections import deque
input = sys.stdin.readline

def solution(n, k, A):
    cnt = 0
    belt = deque([False] * n) # 벨트 위에 로봇 유무

    while True:
        cnt += 1
        
        belt[n-1] = False # 내리기 위치에 있는 로봇 먼저 내리고 회전시키기

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다. (시계방향으로 회전)
        belt.rotate(1)
        A.rotate(1)

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        belt[n-1] = False # 내리기 위치에 있는 로봇 내리기

        for i in range(n-2, -1, -1):
            if A[i+1] > 0 and belt[i] and not belt[i+1]: # 현재 벨트 위에 로봇이 있고, 다음 벨트 위에 로봇이 없으며 다음 벨트의 칸에 내구도가 1 이상
                belt[i], belt[i+1] = False, True
                A[i+1] -= 1 

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        if A[0] > 0:
            belt[0] = True
            A[0] -= 1
    
        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        if A.count(0) >= k:
            break

    return cnt


n, k = map(int, input().split())
A = deque(list(map(int, input().split())))

print(solution(n, k, A))