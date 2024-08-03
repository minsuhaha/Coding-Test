def solution(n, times):
    answer = 0
    start, end = times[0], times[-1]*n # 최소시간을 start, 최대시간을 end
    while start <= end:
        total = 0
        mid = (start+end) // 2
        for time in times:
            total += mid//time
        
        if total >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer