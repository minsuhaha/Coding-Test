def solution(s):
    ans = []
    
    if len(s) == 1:
        return 1
    for i in range(1, len(s)): # 단위기준
        string = s[:i]
        cnt = 1
        res = ''
        for j in range(i, len(s), i):
            if s[j:j+i] == string:
                cnt += 1
            else:
                if cnt >= 2:
                    res += str(cnt) + string
                else:
                    res += string
                cnt = 1
                string = s[j:j+i]
        
        if cnt >= 2:
            res += str(cnt) + string
        else:
            res += string
        ans.append(len(res))
    return min(ans)    
            
                