import sys
input = sys.stdin.readline

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
line.sort(key=lambda x:x[0])

start, end = line[0][0], line[0][1]
cnt = 0
for i in range(1, N):
    if line[i][0] <= end and line[i][1] > end:
        end = line[i][1]
    elif line[i][0] > end:
        cnt += (end-start) # 선분 한개 길이 더해주기
        start = line[i][0]
        end = line[i][1]
cnt += (end - start)
print(cnt)