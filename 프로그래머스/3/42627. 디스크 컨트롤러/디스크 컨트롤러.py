import heapq
def solution(jobs):
    q = []
    prior = -1
    now = 0
    total_work = 0
    finish = 0
    while finish < len(jobs):
        for job in jobs:
            if prior < job[0] <= now:
                heapq.heappush(q, (job[1], job[0]))
        
        if q:
            work_time, start_time = heapq.heappop(q)
            prior = now
            now += work_time
            total_work += (work_time + prior - start_time)
            finish += 1
        else:
            now += 1
    
    return total_work // len(jobs)
            