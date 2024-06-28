import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    w = input().rstrip()
    k = int(input())

    dict = defaultdict(list)
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            dict[w[i]].append(i)
    
    if dict:
        result = []
        for dict_value in dict.values():
            for i in range(len(dict_value)-k+1):
                result.append(dict_value[i+k-1] - dict_value[i] + 1)
        print(min(result), max(result))
    else:
        print(-1)
