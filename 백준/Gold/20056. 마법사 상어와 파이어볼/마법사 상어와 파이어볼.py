import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(n)]
fireball = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split()) # r:행, c:열, m:질량, s:속도, d:방향
    fireball.append((r-1, c-1, m, s, d))

move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for _ in range(k):
    while fireball:
        r, c, m, s, d = fireball.pop()
        r = (r + move[d][0]*s) % n
        c = (c + move[d][1]*s) % n
        graph[r][c].append((m, s, d)) # 질량, 속도, 방향

    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) == 1:
                _m, _s, _d = graph[i][j].pop()
                fireball.append((i, j, _m, _s, _d))

            elif len(graph[i][j]) >= 2:
                sum_m, sum_s, even_cnt, odd_cnt, cnt = 0, 0, 0, 0, len(graph[i][j])
                while graph[i][j]:
                    _m, _s, _d = graph[i][j].pop()
                    sum_m += _m
                    sum_s += _s
                    if _d % 2 == 0:
                        even_cnt += 1
                    else:
                        odd_cnt += 1
                
                if even_cnt == cnt or odd_cnt == cnt:
                    direction = [0, 2, 4, 6]
                else:
                    direction = [1, 3, 5, 7]

                if sum_m // 5 != 0:
                    for d in direction:
                        fireball.append((i, j, sum_m//5, sum_s //cnt , d))
                        
print(sum(ball[2] for ball in fireball))
