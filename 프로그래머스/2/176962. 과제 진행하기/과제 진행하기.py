def time_revert(start):
    hour, minute = map(int, start.split(':'))
    time = hour*60 + minute
    return time

def solution(plans):
    answer = []
    
    # 1. start -> 분으로 변환 및 start 시간 기준으로 오름차순으로 정렬
    plans = [[name, time_revert(start), int(playtime)] for name, start, playtime in plans]
    plans.sort(key=lambda x:x[1])
    
    # 2. plans의 수만큼 루프 돌리기 -> 제일 마지막 start가 실행이 되기까지 파악
    stack = []
    for i in range(len(plans)):
        name, start, playtime = plans[i] # 진행 중 인 현재 과제
        
        while stack:
            _name, _playtime = stack.pop()
            if left_time >= _playtime:
                left_time -= _playtime
                answer.append(_name)
            else:
                _playtime -= left_time
                stack.append((_name, _playtime))
                break
        
        if i < len(plans)-1: # 마지막 인덱스가 아닐 때
            next_plan = plans[i+1]
            left_time = next_plan[1] - start 
            
        stack.append((name, playtime))
    
    # 3. stack에 남아 있는 과제들을 후입선출 방식으로 answer 값에 담아줌 -> 가장 최근 들어온 과제를 가장 먼저 실행시키고 종료해야 됨으로
    for _ in range(len(stack)):
        answer.append(stack.pop()[0])
    
    return answer