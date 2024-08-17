def solution(storey):
    cnt = 0
    while storey > 0:
        num1 = storey % 10 # 일의자리 수 뽑기
        num2 = (storey // 10) % 10 # 다음 자리 수 뽑기
        
        if num1 > 5:
            cnt += (10-num1)
            storey += (10-num1)
        elif num1 < 5:
            cnt += num1
            storey -= num1
        else: # num1 = 5 일 경우
            if num2 >= 5:
                cnt += num1
                storey += num1
            elif num2 < 5:
                cnt += num1
                storey -= num1
        storey //= 10
    return cnt