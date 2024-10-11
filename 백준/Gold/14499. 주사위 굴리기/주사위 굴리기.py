import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0] # 가장 처음에 주사위에는 모든 면에 0
move = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동, 서, 북, 남

def dice_move(d):
    # 동쪽
    if d == 0: 
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 서쪽
    elif d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 북쪽
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    # 남쪽
    elif d == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    return dice

for d in direction:
    nx = x + move[d-1][0]
    ny = y + move[d-1][1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    
    dice_move(d-1) # 주사위 방향으로 굴림

    # 1. 칸에 있는 수가 0일때, 주사위 바닥면에 쓰여있는 수가 칸에 복사
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    
    # 2. 칸에 적혀있는 수가 0이 아니라면, 칸에 쓰여있는 수가 주사위 바닥면으로 복사되고, 칸은 0
    elif board[nx][ny] > 0:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    
    x, y = nx, ny

    print(dice[0])
    