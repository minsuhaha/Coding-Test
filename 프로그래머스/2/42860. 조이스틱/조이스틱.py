import string
def solution(name):
    alpha_dict = {}
    new_value = 12
    for idx, alpha in enumerate(string.ascii_uppercase):
        if idx > 13:
            idx = new_value
            new_value -= 1
        alpha_dict[alpha] = idx
        
    cnt = 0
    # 상하 커서 이동
    for n in name:
        cnt += alpha_dict[n]
    
    # 좌우 커서 이동
    n = len(name)
    distance = n - 1 # 오른쪽으로만 이동 할 경우
    for i in range(n):
        next_move = i + 1
        
        # 연속되는 A 문자열 끝 값
        while next_move < n and name[next_move] == 'A':
            next_move += 1
            
        distance = min(distance, i*2 + n-next_move)
        distance = min(distance, (n-next_move)*2 + i)
        
    return cnt + distance