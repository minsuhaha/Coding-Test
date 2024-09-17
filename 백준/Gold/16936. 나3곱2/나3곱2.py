import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
B = list(map(int, input().split()))
check_dict = defaultdict(int)
for b in B:
    check_dict[b] = 1


def dfs(num):
    
    if len(res) == n:
        print(*res)
        exit()
    
    if num % 3 == 0 and check_dict[num//3] > 0:
        check_dict[num//3] -= 1
        res.append(num//3)
        dfs(num//3)
        res.pop()
        check_dict[num//3] += 1

    if check_dict[num*2] > 0:
        check_dict[num*2] -= 1
        res.append(num*2)
        dfs(num*2)
        res.pop()
        check_dict[num*2] += 1

res = []
for b in B:
    check_dict[b] -= 1
    res.append(b)
    dfs(b)
    res.pop()
    check_dict[b] += 1
