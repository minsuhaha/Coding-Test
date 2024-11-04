from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_queue = deque(truck_weights)
    move_truck = deque([0]*bridge_length)
    total_weight = 0
    second = 0
    
    while truck_queue:
        second += 1
        total_weight -= move_truck.popleft() # 1초 지났으니 다리 이동시킴
        
        if total_weight + truck_queue[0] <= weight:
            total_weight += truck_queue[0]
            move_truck.append(truck_queue.popleft()) # 대기 트럭 다리로 이동
        else:
            move_truck.append(0)
    
    return second + bridge_length
        