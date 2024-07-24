def solution(s):
    dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 
            'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    res, num_str = '',''
    for num in s:
        num_str += num
        if num_str in dict.keys():
            res += dict[num_str]
            num_str = ''
        if not num.isalpha():
            res += num
            num_str = ''

    return int(res)
            
        
        
        