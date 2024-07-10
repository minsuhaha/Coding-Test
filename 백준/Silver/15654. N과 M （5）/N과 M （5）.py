import sys
input = sys.stdin.readline


def back():
    if len(res) == M:
        print(*res)
        return
    
    for l in lst:
        if l not in res:
            res.append(l)
            back()
            res.pop()

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
res = []
back()
