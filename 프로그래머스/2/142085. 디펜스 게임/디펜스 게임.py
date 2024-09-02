import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    
    for i in range(len(enemy)):
        heapq.heappush(heap, enemy[i])
        
        if len(heap) > k:
            n -= heapq.heappop(heap)
            if n < 0:
                break
        answer += 1
    return answer
        