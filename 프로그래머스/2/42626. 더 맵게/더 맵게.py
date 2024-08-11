import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        new_food = 0
        food_1 = heapq.heappop(scoville)
        food_2 = heapq.heappop(scoville)
        
        new_food = food_1 + (food_2*2)
        heapq.heappush(scoville, new_food)
        cnt += 1
    
    return cnt
        
    
    
    
    