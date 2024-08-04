from collections import defaultdict
def solution(clothes):
    clothes_dict = defaultdict(list)
    for i in range(len(clothes)):
        clothes_dict[clothes[i][1]].append(clothes[i][0])
        
    answer = 1
    for key in clothes_dict.keys():
        answer *= (len(clothes_dict[key])+1)
    return answer - 1
        
            