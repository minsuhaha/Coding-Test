import sys
input = sys.stdin.readline


def back():
    if len(res) == M:
        print(*res)
        return
    
    prev = 0
    for i in range(N):
        if prev != lst[i] and not visited[i]:
            res.append(lst[i])
            visited[i] = True # 똑같은 위치의 값이 중복되는것을 방지
            prev = lst[i]
            back()
            res.pop()
            visited[i] = False

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
res = []
visited = [False] * N
back()
