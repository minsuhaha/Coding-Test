import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x:x[0])
heap = []
heapq.heappush(heap, time[0][1]) # 기본 : 최소 힙

for i in range(1, N):
    if time[i][0] >= heap[0]:
        heapq.heappop(heap) # 가장 앞단에 있는 값 제거
    heapq.heappush(heap, time[i][1])

print(len(heap))