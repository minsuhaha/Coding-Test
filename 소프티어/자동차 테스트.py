import sys
from bisect import bisect_left
input = sys.stdin.readline

n, q = map(int, input().split())
cars = sorted(map(int, input().split()))
set_cars = set(cars)

for _ in range(q):
    m = int(input())

    # 1. m 값은 cars 배열안에 있는 값이여야 함
    if m not in set_cars:
        print(0)
        continue

    # 2. m은 자신보다 작거나 큰 경우의 개수가 둘다 1이상 이여야 함
    idx = bisect_left(cars, m)
    if idx == 0 or idx == n-1:
        print(0)
        continue

    print(idx * (n-1-idx))
    