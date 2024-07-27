def solution(data, col, row_begin, row_end):
    # 1. 주어진 col칼럼값을 기준으로 오름차순 정렬
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    # 2. row_begin <= i <= row_end 각 i번째 행에 대해 나눠주기
    total = 0
    for i in range(row_begin, row_end+1):
        result = 0
        for d in data[i-1]:
            result += (d%(i))
        total ^= result
    return total

