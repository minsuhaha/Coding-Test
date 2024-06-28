import sys
input = sys.stdin.readline

# 그룹 수로 생각해보자
n = int(input())
k = int(input())
sensor = sorted(map(int,input().split()))
diff = []

for i in range(n-1):
    diff.append(sensor[i+1]-sensor[i])
diff.sort(reverse=True)

print(sum(diff[k-1:]))

