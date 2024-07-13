import sys
input = sys.stdin.readline


def back(start):
    if len(res) == L:
        cnt1, cnt2 = 0, 0
        for r in res:
            if r in 'aeiou':
                cnt1 += 1
            else:
                cnt2 += 1

        if cnt1 >= 1 and cnt2 >= 2:
            print(''.join(res))
        return
    
    for i in range(start, C):
        res.append(string[i])
        back(i+1)
        res.pop()

L, C = map(int, input().split())
string = sorted(input().rstrip().split())
res = []
back(0)
