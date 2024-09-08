from collections import defaultdict
def solution(tickets):
    
    def dfs(city):
        
        while tickets_dict[city]:
            next_city = tickets_dict[city].pop(0)
            dfs(next_city)
        res.append(city)
        
    tickets_dict = defaultdict(list)
    for a, b in tickets:
        tickets_dict[a].append(b)
    for city in tickets_dict:
        tickets_dict[city].sort() # 오름차순으로 정렬
    
    res = []
    dfs('ICN')
    return res[::-1]
        
        