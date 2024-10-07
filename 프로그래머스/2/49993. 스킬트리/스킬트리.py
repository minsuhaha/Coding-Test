from collections import defaultdict
def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        skill_order = []
        for st in skill_tree:
            if st in skill:
                skill_order.append(st)
        if ''.join(skill_order) == skill[:len(skill_order)]:
            cnt += 1
    return cnt
        
            
        
    
    
