'''
1. 주사위 만들기 -> 바라보는 면 합이 7  / 1행1열 + 초기 오른쪽 방향
2. 주사위가 움직임
    - 주사위가 놓여있는 칸에 적혀있는 숫자와 상하좌우 숫자 비교 -> 동일숫자면 합산 : 점수
    - 주사위 아랫면 > 해단 칸 숫자 -> 90도 시계방향으로 회전
    - 주사위 아랫면 < 해단 칸 숫자 -> 90도 반시계방향으로 회전
    - 주사위 아랫면 = 해당 칸 숫자 -> 그대로
* 진행도중 격자판을 벗어나게 된다면, 반대방향(180도회전)으로 방향바꾸고 한칸 움직임.
'''
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 6, 2, 3, 5, 4]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상

def dice_change(d):
    # 우
    if d == 0:
        dice[0], dice[1], dice[3], dice[5] = dice[5], dice[3], dice[0], dice[1]
    # 하
    elif d == 1:
        dice[0], dice[1], dice[2], dice[4] = dice[4], dice[2], dice[0], dice[1]
    # 좌
    elif d == 2:
        dice[0], dice[1], dice[3], dice[5] = dice[3], dice[5], dice[1], dice[0]
    # 상
    elif d == 3:
        dice[0], dice[1], dice[2], dice[4] = dice[2], dice[4], dice[1], dice[0]


def calculator(x, y):
    queue = deque([(x, y)])
    cnt = graph[x][y]
    visited = set([(x, y)])
    total = cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            cx, cy = x + move[i][0], y + move[i][1]

            if 0<=cx<n and 0<=cy<n and (cx, cy) not in visited:
                if graph[cx][cy] == cnt:
                    queue.append((cx, cy))
                    visited.add((cx, cy))
                    total += cnt
    return total

x, y = 0, 0 # 주사위 초기 위치 1행
d = 0
score = 0
for _ in range(m):
    nx = x + move[d][0]
    ny = y + move[d][1]

    # 진행도중 격자판을 벗어나게 된다면, 반대방향(180도회전)으로 방향바꾸고 한칸 움직임
    if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
        d = (d+2) % 4
        nx = x + move[d][0]
        ny = y + move[d][1]
    
    # 주사위 굴리기
    dice_change(d)

    # 주사위가 놓여있는 칸에 적혀있는 숫자와 상하좌우 숫자 비교 -> 동일숫자면 합산 : 점수
    score += calculator(nx, ny)

    # 주사위 방향 결정
    if dice[1] > graph[nx][ny]:
        d = (d+1) % 4
    elif dice[1] < graph[nx][ny]:
        d = (d+3) % 4
    
    x, y = nx, ny

print(score)