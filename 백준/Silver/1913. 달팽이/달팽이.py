import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

board = [[0]*n for _ in range(n)]

trans = 1
num = n*n
row, col = -1, 0
ax, ay = 0, 0

while n > 0:
    for i in range(n):
        row += trans
        board[row][col] = num
        if num == m:
            ax, ay = row+1, col+1
        num -= 1

    n -= 1

    for i in range(n):
        col += trans
        board[row][col] = num
        if num == m:
            ax, ay = row+1, col+1
        num -= 1

    trans *= -1

for b in board:
    print(*b)
print(ax, ay)
