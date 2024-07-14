import sys
input = sys.stdin.readline


def back():
    if len(res) == len(word):
        print(''.join(res))
        return
    
    prev = ''
    for i in range(len(word)):
        if word[i] != prev and not visited[i]:
            res.append(word[i])
            visited[i] = True
            prev = word[i]
            back()
            res.pop()
            visited[i] = False


N = int(input())
for _ in range(N):
    word = sorted(input().rstrip())
    res = []
    visited = [False] * len(word)
    back()
