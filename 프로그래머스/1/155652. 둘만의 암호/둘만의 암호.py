# a -> 97 z -> 122  : 25차이  ord사용
# 97 -> a 122 -> z chr사용
import string
def solution(s, skip, index):
    alpha_dict = {string.ascii_lowercase[i]:i for i in range(26)}
    num_dict = {i:string.ascii_lowercase[i] for i in range(26)}
    
    result = []
    for alp in s:
        cnt = 0
        next_alp = alp
        while cnt < index:
            n_alp = (alpha_dict[next_alp]+1) % 26
            if num_dict[n_alp] not in skip:
                cnt += 1
            next_alp = num_dict[n_alp]
                
        result.append(next_alp)
    return ''.join(result)
                