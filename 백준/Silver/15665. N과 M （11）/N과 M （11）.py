import sys
input = sys.stdin.readline


def back():
    if len(res) == M:
        print(*res)
        return
    
    prev = 0
    for i in range(N):
        if prev != lst[i]:
            res.append(lst[i])
            prev = lst[i]
            back()
            res.pop()


N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
res = []
back()
