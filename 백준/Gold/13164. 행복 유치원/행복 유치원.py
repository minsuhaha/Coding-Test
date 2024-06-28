# 조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다.
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

height = list(map(int,input().split()))
diff = [] # 인접 학생 차이 값 넣기
for i in range(n-1):
    diff.append(height[i+1] - height[i]) # 인접 학생 차이 값


total = 0
diff.sort() # 최솟값을 구해야되니깐 차이가 작은 값부터 정렬
if n == k:
    pass
else:
    for i in range(n-k):
        total += diff[i]
print(total)