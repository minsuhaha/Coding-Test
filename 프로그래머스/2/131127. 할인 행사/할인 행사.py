from collections import Counter
def solution(want, number, discount):
    want_count = {}
    for i in range(len(number)):
        want_count[want[i]] = number[i]
        
    cnt = 0
    for i in range(len(discount)-9):
        if want_count == Counter(discount[i:i+10]):
            cnt += 1
    return cnt