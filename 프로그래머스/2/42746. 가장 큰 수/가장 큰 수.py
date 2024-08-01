def solution(numbers):
    # 사전식 비교 (문자열 활용 -> 문자열에서는 앞의 원소만 비교함)
    numbers = list(map(str, numbers)) 
    numbers.sort(key=lambda x:x*3, reverse=True)
    
    return '0' if all(num == '0' for num in numbers) else ''.join(numbers)