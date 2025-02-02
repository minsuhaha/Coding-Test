from collections import deque
n, k = map(int, input().split())

queue = deque(x for x in range(1, n+1)) # 1~N 까지의 사람들을 queue에 list 형태로 담아주기
answer = []

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft()) # 가장 앞에 있는 사람을 pop 한 후 queue 큐에 가장 뒤에 위치시키기
    answer.append(queue.popleft()) # k번째 사람을 제거

print(str(answer).replace('[','<').replace(']','>'))
