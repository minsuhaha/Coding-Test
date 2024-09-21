import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = False
cnt = 10**6
for i in range(1, n+1):
    for j in graph[i]:
        if j > i:
            for k in graph[j]:
                if k > j and i in graph[k]:
                    cnt = min(cnt, len(graph[i])+len(graph[j])+ len(graph[k]) - 6)
                    flag = True

if flag:
    print(cnt)
else:
    print(-1)
