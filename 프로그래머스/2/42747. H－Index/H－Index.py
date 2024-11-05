def solution(citations):
    citations.sort(reverse=True)
    
    # [6, 5, 3, 1, 0]
    for idx, citation in enumerate(citations):
        if idx+1 > citation:
            return idx
    return idx+1
    
    