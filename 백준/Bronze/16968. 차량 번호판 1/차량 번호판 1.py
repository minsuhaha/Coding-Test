import sys, string
input = sys.stdin.readline

num = input().rstrip()

def dfs(idx, prior):
    global cnt
    if idx == len(num):
        cnt += 1
        return
    
    if num[idx] == 'c':
        for i in range(len(string.ascii_lowercase)):
            if prior != string.ascii_lowercase[i]:
                dfs(idx+1, string.ascii_lowercase[i])

    else:
        for i in range(10):
            if prior != str(i):
                dfs(idx+1, str(i))

cnt = 0
dfs(0, '')
print(cnt)
