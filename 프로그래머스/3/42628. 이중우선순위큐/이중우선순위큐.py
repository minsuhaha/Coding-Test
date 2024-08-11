import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        cal, num = operation.split()
        if cal == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        elif cal == 'D' and min_heap: 
            if num == '-1':
                n = heapq.heappop(min_heap)
                max_heap.remove(-n)     
            elif num == '1':
                n = heapq.heappop(max_heap)
                min_heap.remove(-n)
    if min_heap:
        min_num, max_num = heapq.heappop(min_heap), -heapq.heappop(max_heap)
        return max_num, min_num
    return 0, 0