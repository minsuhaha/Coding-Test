import sys
import heapq
input = sys.stdin.readline

n = int(input())
course = [list(map(int, input().split())) for _ in range(n)]
course.sort(key=lambda x:x[0]) # 끝나는 시간 기준으로 오름차순 정렬

heap = [] # 항상 오름차순으로 정렬 된 상태로 있도록 하기 위해
heapq.heappush(heap, course[0][1]) # 첫 강의 시작 값은 있어야 하기에
for i in range(1, len(course)):
    if course[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, course[i][1])

print(len(heap))
