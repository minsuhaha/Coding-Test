import sys
input = sys.stdin.readline

prime = [] # 소수를 담을 리스트
check = [0] * 1000001
for i in range(2, int(1000001**0.5)+1): # 주어진 조건이 100000이하의 짝수범위라서
    if check[i] == 0:
        prime.append(i)
    for i in range(i**2, 1000001, i):
        check[i] = 1 # 소수 아님

while True:
    n = int(input())
    if n == 0:
        break
    else:
        flag = False
        for p in prime:
            is_prime = n - p
            if not check[is_prime]: # 소수라면
                print(f'{n} = {p} + {is_prime}')
                flag = True
                break
        if not flag:
            print("Goldbach's conjecture is wrong")
