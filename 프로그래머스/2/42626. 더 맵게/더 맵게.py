import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # 기본값 : 최소값부터 오름차순 정렬
    cnt = 0
    while scoville[0] < K:
        first = heapq.heappop(scoville)
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first+(second*2))
        cnt += 1
        
    return cnt
    
    