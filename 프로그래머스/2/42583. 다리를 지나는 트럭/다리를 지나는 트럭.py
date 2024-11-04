from collections import deque
def solution(bridge_length, weight, truck_weights):
    lst = [0] * bridge_length
    bridge = deque(lst)
    queue = deque(truck_weights)
    
    total_weight = 0
    minute = 0
    while queue:
        minute += 1
        w = queue[0]
        total_weight -= bridge.popleft()
        
        if total_weight + w <= weight:
            total_weight += queue.popleft()
            bridge.append(w)
        else:
            bridge.append(0)

    return minute + bridge_length  