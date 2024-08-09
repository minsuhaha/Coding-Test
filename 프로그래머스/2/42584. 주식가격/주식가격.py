from collections import deque
def solution(prices):
    prices_q = deque(prices)
    answer = []
    
    while prices_q:
        time = 0
        price = prices_q.popleft()
        
        for p in prices_q:
            time += 1
            if price > p:
                break
        answer.append(time)
    
    return answer
                
    
            
        