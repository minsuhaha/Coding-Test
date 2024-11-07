from collections import defaultdict
def solution(tickets):
    ticket_dict = defaultdict(list)
    for start, end in tickets:
        ticket_dict[start].append(end)
    
    for key, value in ticket_dict.items():
        value.sort(reverse=True)
    
    def dfs(node):
        while ticket_dict[node]:
            next_node = ticket_dict[node].pop()
            dfs(next_node)
        res.append(node)
        
    res = []
    dfs('ICN')
    return res[::-1]