import sys
input = sys.stdin.readline

def back(start):
    if len(res) == 6:
        print(*res)
        return
    
    for i in range(start, K):
        res.append(S[i])
        back(i+1)
        res.pop()

while True:
    lst = list(map(int, input().split()))
    K = lst[0]
    if not K:
        break
    S = lst[1:]

    res = []
    back(0)

    print()
