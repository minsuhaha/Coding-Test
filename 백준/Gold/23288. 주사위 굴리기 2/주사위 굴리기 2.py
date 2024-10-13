'''
1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    A = B인 경우 이동 방향에 변화는 없다.
    * 칸 (x, y)에 대한 점수는 다음과 같이 구할 수 있다. (x, y)에 있는 정수를 B라고 했을때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다. 
     이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. 여기서 점수는 B와 C를 곱한 값이다.
    * 가장 처음에 주사위의 이동 방향은 동쪽이다
'''
import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 2, 3, 4, 5, 6] # 윗면, 앞, 오, 왼, 뒤, 아랫면
move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 동남서북

def dice_move(d):
    # 동
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 남
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    # 서
    elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 북
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]


def calculate_score(x, y, B):
    queue = deque([(x, y)])
    visited = set([(x, y)])
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + move[i][0]
            ny = cy + move[i][1]

            if 0<=nx<n and 0<=ny<m:
                if (nx, ny) not in visited and board[nx][ny] == B:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
    C = len(visited)
    score = B * C 
    return score

d = 0
x, y = 0, 0
score = 0

for _ in range(k):
    # 1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    nx = x + move[d][0]
    ny = y + move[d][1]
    
    if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
        d = (d + 2) % 4
        nx = x + move[d][0]
        ny = y + move[d][1]
    
    dice_move(d) # 주사위 한 칸 굴러감

    # 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    B = board[nx][ny]
    score += calculate_score(nx, ny, B)

    # 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    A = dice[5]
    if A > B:
        d = (d+1) % 4
    elif A < B:
        d = (d+3) % 4

    x, y = nx, ny

print(score)
