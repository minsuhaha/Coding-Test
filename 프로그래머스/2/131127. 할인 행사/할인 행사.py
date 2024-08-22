from collections import Counter
def solution(want, number, discount):
    res = 0
    want_dict = {}
    for w, n in zip(want, number):
        want_dict[w] = n
    
    discount_cnt = Counter(discount[:10])
    
    if discount_cnt == want_dict:
        res += 1

    for i in range(10, len(discount)):
        discount_cnt[discount[i]] += 1
        discount_cnt[discount[i-10]] -= 1
        
        if discount_cnt[discount[i-10]] == 0:
            del discount_cnt[discount[i-10]]
            
        if discount_cnt == want_dict:
            res += 1
        
    return res
                
        