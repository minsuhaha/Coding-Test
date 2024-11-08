def solution(n, words):
    people = {i:[] for i in range(1, n+1)}
    
    idx = 1
    people[idx].append(words[0]) 
    words_set = set([words[0]]) # 등장한 문자
    prior = words[0][-1] # 이전 단어 마지막 문자

    for word in words[1:]:
        if idx + 1 > n:
            idx = 1
        else:
            idx += 1
        people[idx].append(word)
        
        # 1. 앞사람이 말한 단어의 마지막 문자와 다르다면 / 2. 이전에 등장한 단어라면
        if word[0] != prior or word in words_set:
            return [idx, len(people[idx])]
        
        prior = word[-1]
        words_set.add(word)
        
    return [0,0]
        
            
        