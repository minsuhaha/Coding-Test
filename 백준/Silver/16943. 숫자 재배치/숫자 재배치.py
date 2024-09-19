'''
A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만들려고 한다. 즉, C는 A의 순열 중 하나가 되어야 한다. 
C 중에서 B보다 작으면서, 가장 큰 값을 구해보자. 
C는 0으로 시작하면 안 된다.
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())


def dfs(res):
    global max_num
    if len(res) == len(str_a):
        if int(res) < b:
            max_num = max(max_num, int(res))
        return
    
    for i in range(len(str_a)):
        if not res and str_a[i] == '0':
            continue
        if not visited[i]:
            visited[i] = True
            dfs(res+str_a[i])
            visited[i] = False

max_num = 0
str_a = str(a)
visited = [False] * len(str_a)
dfs('')
if max_num:
    print(max_num)
else:
    print(-1)
    