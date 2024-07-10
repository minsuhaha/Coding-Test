import sys
input = sys.stdin.readline


def back():
    if len(res) == M:
        print(*res)
        return 
    
    for i in range(1, N+1):
        if i not in res:
            res.append(i)
            back()
            res.pop()

N, M = map(int, input().split())
res = []
back()
