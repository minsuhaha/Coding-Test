from collections import defaultdict
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(words):
        nonlocal rank
        if len(words) == 5:
            return
        
        for alp in alpha:
            if words+alp not in res:
                rank += 1
                res[words+alp] = rank
                dfs(words+alp)
                
    res = defaultdict(int)
    rank = 0
    dfs('')
    return res[word]