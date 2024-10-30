'''
* 주사위 이동방향순서 : 동쪽 -> 서쪽 -> 북쪽 -> 남쪽
1. 주사위 생성 (초기 값 0)
2. 주사위 이동
    - d방향으로 1칸씩 이동
    - 이동 후 칸에 쓰여있는 수가 0이면 -> 주사위 바닥면에 쓰여져있는 수를 칸에 복사
    - 이동 후 칸에 쓰여있는 수가 0이 아니면 -> 칸에 쓰여져있는 수 주사위 바닥면으로 복사 후 칸의 수 0
    * 주사위는 격자판 밖으로 이동불가
'''
import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
d = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0] # 주사위 생성
move = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남

def dice_roll(d):
    if d == 1:
        dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]
    elif d == 2:
        dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
    elif d == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
    elif d == 4:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]


for i in range(k):
    nx = x + move[d[i]-1][0]
    ny = y + move[d[i]-1][1]

    if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
        continue
    
    dice_roll(d[i]) # 주사위 굴리기

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[4] # 주사위 바닥면 칸에 복사
    else:
        dice[4] = graph[nx][ny]
        graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[5])