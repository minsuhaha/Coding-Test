import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    for operation in operations:
        oper, num = operation.split()
        if oper == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        elif oper == 'D':
            if len(min_heap) == 0:
                continue
            elif num == '1':
                q = heapq.heappop(max_heap)
                min_heap.remove(-q)
            elif num == '-1':
                q = heapq.heappop(min_heap)
                max_heap.remove(-q)
    if min_heap:
        return -heapq.heappop(max_heap), heapq.heappop(min_heap)
    return [0,0]
    