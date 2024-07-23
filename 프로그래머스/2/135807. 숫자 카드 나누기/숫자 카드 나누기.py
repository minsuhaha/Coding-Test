def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(arrayA, arrayB):
    A_cnt = arrayA[0]
    for a in arrayA[1:]:
        A_cnt = min(A_cnt, gcd(A_cnt, a))
    
    B_cnt = arrayB[0]
    for b in arrayB[1:]:
        B_cnt = min(B_cnt, gcd(B_cnt, b))
        
    flag_B = True # B_cnt로 arrayA 원소중 나눠지는게 있는가
    for a in arrayA:
        if a % B_cnt == 0:
            flag_B = False
            break
    
    flag_A = True # A_cnt로 arrayB 원소중 나눠지는게 있는가
    for b in arrayB:
        if b % A_cnt == 0:
            flag_A = False
            break
            
    
    if not flag_A and not flag_B: # 둘다 나눠질 때
        return 0
    elif flag_A and flag_B: # 둘다 나눠지지 않은 수일 때
        return max(A_cnt, B_cnt)
    elif not flag_A:
        return B_cnt
    elif not flag_B:
        return A_cnt   

# 1. arrayA or arrayB 각각 최대공약수 중 큰 값 뽑기 
# 2. 뽑은 값을 다른 array 원소중에 나눠지는지 파악하기
# 3. 나눠진다면 해당 값이 가장 큰 양의 정수 a임
# arrayA / arrayB 
# arrayA or arrayB -> 최대공약수 뽑기