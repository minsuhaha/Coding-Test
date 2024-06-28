# 입국심사
n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]

def binary(n, times):
    start = 1
    end = max(times)*m
    while start <= end:
        mid = (start+end) // 2
        cnt = 0
        for i in range(n):
            cnt += (mid // times[i])
        if cnt >= m:
            end = mid - 1
        elif cnt < m:
            start = mid + 1
    return start
 
result = binary(n, times)
print(result)