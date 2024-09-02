from collections import deque
def solution(begin, target, words):
    
    def bfs(begin, count):
        queue = deque([(begin, count)])
        
        while queue:
            word, count = queue.popleft()
            
            if word == target:
                return count
            
            for i in range(len(words)):
                cnt = 0
                if not visited[i]:
                    for j in range(len(words[i])):
                        if word[j] == words[i][j]:
                            cnt += 1
                        if cnt == len(words[i])-1:
                            queue.append((words[i], count+1))
                            visited[i] = True
        return 0
    
    visited = [False] * len(words)
    return bfs(begin, 0)
    
    
    
    
    
    
#     def dfs(now_word, count):
#         nonlocal answer
#         if now_word == target:
#             answer = min(answer, count)
#             return
    
#         for i in range(len(words)):
#             cnt = 0
#             for j in range(len(words[i])):
#                 if now_word[j] == words[j]:
#                     cnt += 1
#                 if cnt == 2:
#                     dfs(words[i], count+1)
            
#     answer = 10000
#     dfs(begin, 0)
#     return answer