def solution(routes):
    routes.sort(key=lambda x:x[1])
    
    cnt = 1
    spot = routes[0][1] # -15
    for i in range(1, len(routes)):
        if routes[i][0] > spot:
            spot = routes[i][1]
            cnt += 1
    
    return cnt
            
        
    