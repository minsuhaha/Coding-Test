def solution(want, number, discount):
    want_dict = {}
    res = 0
    
    for i in range(len(discount)-9):
        for w, n in zip(want, number):
            want_dict[w] = n
            
        for d in discount[i:i+10]:
            if d in want_dict.keys():
                want_dict[d] -= 1
            elif d not in want_dict.keys():
                break
        
        flag = True
        for key, value in want_dict.items():
            if value != 0:
                flag = False
                break
        
        if flag:
            res += 1
        
    return res
                
        