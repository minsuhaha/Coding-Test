import copy
from collections import defaultdict
def solution(skill, skill_trees):
    skill_dict = {s:[] for s in skill}
    indegree = {s:0 for s in skill}
    
    for i in range(len(skill)-1):
        for j in range(i+1, len(skill)):
            skill_dict[skill[i]].append(skill[j])
            indegree[skill[j]] += 1
    
    cnt = 0
    for skill_tree in skill_trees:
        indegree_copy = copy.deepcopy(indegree)
        flag = True
        for skill in skill_tree:
            if skill not in skill_dict:
                continue
            if indegree_copy[skill] > 0:
                flag = False
                break
            if indegree_copy[skill] == 0:
                for s in skill_dict[skill]:
                    indegree_copy[s] -= 1
    
        if flag:
            cnt += 1
    return cnt   
                
    