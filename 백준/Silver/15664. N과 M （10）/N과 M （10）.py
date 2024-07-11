import sys
input = sys.stdin.readline

def back(start):
    if len(res) == M:
        print(*res)
        return
    
    prev = 0
    for i in range(start, N):
        if prev != lst[i]:
            res.append(lst[i])
            prev = lst[i]
            back(i+1)
            res.pop()


N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
res = []
back(0)
