import sys
input = sys.stdin.readline

m, n = map(int, input().split())

board = [[0]*n for _ in range(m)]

# 오, 아래, 왼, 위
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
total = m*n
now = 0
row, col = 0, -1
dir = 0

cnt = 0
while now < total:
    next_row = row + move[dir][0]
    next_col = col + move[dir][1]

    if 0<=next_row<m and 0<=next_col<n and board[next_row][next_col] == 0:
        board[next_row][next_col] = 1
        now += 1
        row, col = next_row, next_col
    
    else:
        dir = (dir + 1) % 4
        cnt += 1

print(cnt)
