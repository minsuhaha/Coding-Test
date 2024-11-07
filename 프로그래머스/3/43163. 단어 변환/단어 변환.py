from collections import deque
def solution(begin, target, words):
    
    def bfs(word):
        queue = deque([(word, 0)])
        
        while queue:
            word, cnt = queue.popleft()
            
            if word == target:
                return cnt
            
            for w in words:
                if w not in visited:
                    count = 0
                    for i in range(len(w)):
                        if word[i] != w[i]:
                            count += 1
                    if count == 1:
                        visited.add(w)
                        queue.append((w, cnt+1))    
        return 0
    visited = set()
    return bfs(begin)
    