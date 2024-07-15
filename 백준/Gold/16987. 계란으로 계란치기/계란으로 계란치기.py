import sys
input = sys.stdin.readline


def check(eggs):
    cnt = 0
    for egg in eggs:
        if egg[0] <= 0:
            cnt += 1
    return cnt

def dfs(index, eggs):
    global count
    if index == N:
        count = max(count, check(eggs))
        return
    
    # 현 index 위치의 게란이 깨져있다면 바로 오른쪽 다음 계란 들기.
    if eggs[index][0] <= 0:
        dfs(index+1, eggs)

    else:
        is_all_broke = True
        for i in range(N):
            if index != i and eggs[i][0] > 0:
                is_all_broke = False
                eggs[i][0] -= eggs[index][1]
                eggs[index][0] -= eggs[i][1]
                dfs(index+1, eggs)
                eggs[i][0] += eggs[index][1]
                eggs[index][0] += eggs[i][1]
        
        # 현 index 위치의 계란을 제외하고 모두 깨졌다면
        if is_all_broke:
            dfs(N, eggs)
            
N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
count = 0
dfs(0, eggs)
print(count)
