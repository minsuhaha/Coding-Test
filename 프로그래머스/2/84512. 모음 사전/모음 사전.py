def solution(word):
    words = "AEIOU"
    def dfs(prior_word):
        if len(prior_word) == 5:
            return
        
        for i in range(5):
            res.append(prior_word + words[i])
            dfs(prior_word + words[i])
    
    res = []
    dfs('')
    return res.index(word) + 1
            