import heapq
def solution(jobs):
    
    heap = []
    start_time = 0
    before_time = -1
    total = 0
    finish = 0
    while finish < len(jobs):
        for job in jobs:
            if before_time < job[0] <= start_time:
                heapq.heappush(heap, (job[1], job[0]))
        
        if len(heap):
            now_job = heapq.heappop(heap)
            before_time = start_time
            start_time = now_job[0] + before_time
            total += (now_job[0] + before_time - now_job[1])
            finish += 1
        else:
            start_time += 1
                
    return total // len(jobs)
        