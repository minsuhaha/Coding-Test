import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
hit_info = [list(map(int, input().split())) for _ in range(n)]

max_score = 0
# 타순은 고정되어야 하기 때문에 경우의 수 별
for hit_order in permutations(range(1, 9), 8):
    hit_order = list(hit_order[:3]) + [0] + list(hit_order[3:])
    score = 0
    hitter = 0
    # 이닝 별
    for i in range(n):
        out = 0
        base = [0, 0, 0, 0] # 홈,1루,2루,3루
        hit = hit_info[i]

        while out < 3:
            if hit[hit_order[hitter]] == 0:
                out += 1
            elif hit[hit_order[hitter]] == 1:
                score += base[3]
                base = [0, 1, base[1], base[2]]
            elif hit[hit_order[hitter]] == 2:
                score += base[2]+base[3]
                base = [0, 0, 1, base[1]]
            elif hit[hit_order[hitter]] == 3:
                score += base[1]+base[2]+base[3]
                base = [0, 0, 0, 1]
            elif hit[hit_order[hitter]] == 4:
                score += base[1]+base[2]+base[3]+1
                base = [0, 0, 0, 0]

            hitter = (hitter+1) % 9

    max_score = max(max_score, score)

print(max_score)
