import sys
input = sys.stdin.readline


def back():
    if len(res) == M:
        print(*res)
        return
    
    for i in range(N):
        res.append(lst[i])
        back()
        res.pop()

N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
res = []
back()
