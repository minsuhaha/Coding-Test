import sys
input = sys.stdin.readline


def back(start):
    if len(res) == M:
        print(*res)
        return 
    
    for i in range(start, N+1):
        if i not in res:
            res.append(i)
            back(i+1)
            res.pop()


N, M = map(int, input().split())
res = []
back(1)