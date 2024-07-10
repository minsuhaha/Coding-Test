import sys
input = sys.stdin.readline


def back(start):
    if len(res) == M:
        print(*res)
        return
    
    for i in range(start, N+1):
        res.append(i)
        back(i)
        res.pop()

N, M = map(int, input().split())
res = []
back(1)
