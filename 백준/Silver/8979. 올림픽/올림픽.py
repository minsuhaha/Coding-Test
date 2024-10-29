n, k = map(int, input().split())
ranks = [list(map(int, input().split())) for _ in range(n)]
ranks = sorted(ranks, key = lambda x : (x[1], x[2], x[3]), reverse=True) # 내림차순으로4
# 금메달 기준으로 정렬, 금메달 수가 같으면 은메달 수로 정렬, 은메달 수도 같으면 동메달 수로 정렬

# k국가 위치찾기
for i in range(n):
    if ranks[i][0] == k: # 찾고자 하는 k의 위치 파악하기
        idx = i # k가 위치에 있는 인덱스를 찾음

# 동점일 경우 생각
for i in range(n):
    if ranks[idx][1:] == ranks[i][1:]: # 동점일 경우
        idx = i # 동점일시 첫번째 나온 수로 모두 지정되기 때문
        break # 동점일 경우 가장 빨리 나온 수 +1 해주면 됨.

print(idx+1)