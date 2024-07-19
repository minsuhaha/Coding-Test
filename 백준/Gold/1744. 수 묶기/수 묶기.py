import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

plus, minus = [], []
max_total = 0

for i in range(N):
    if nums[i] > 1:
        plus.append(nums[i])
    elif nums[i] <= 0:
        minus.append(nums[i])
    else: # 1일 경우 -> 묶는거보다 합해주는게 낫기 때문
        max_total += nums[i]
    
# 음수 계산
minus.sort()
for i in range(0, len(minus), 2):
    if i+1 > len(minus)-1:
        max_total += minus[i]
    else:
        max_total += (minus[i]*minus[i+1])

# 양수 계산
plus.sort(reverse=True)
for i in range(0, len(plus), 2):
    if i+1 > len(plus)-1:
        max_total += plus[i]
    else:
        max_total += (plus[i]*plus[i+1])

print(max_total)
