from collections import deque
def solution(n, wires):
    answer = 100
    queue = deque([[] for _ in range(n+1)])
    for wire in wires:
        queue[wire[0]].append(wire[1])
        queue[wire[1]].append(wire[0])
    
    def bfs(wire):
        q = deque([wire[0]]) # 복사본
        visited = [False] * (n+1)
        visited[wire[0]] = True
        cnt = 1
        while q:
            node = q.popleft()
            
            for next_node in queue[node]:
                if next_node != wire[1] and not visited[next_node]:
                    visited[next_node] = True
                    cnt += 1
                    q.append(next_node)
                    
        return abs((n-cnt)-cnt)
            
    for i in range(n-1):
        answer = min(bfs(wires[i]), answer)
    return answer