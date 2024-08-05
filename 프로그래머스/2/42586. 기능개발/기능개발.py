def solution(progresses, speeds):
    answer = []
    result = []
    day = 0
    for i in range(len(progresses)):
        time = progresses[i]
        if day:
            time = time + (speeds[i]*day)
        while time < 100:
            time += speeds[i]
            day += 1
        answer.append(day)
    
    cnt = 1
    for i in range(len(answer)-1):
        if answer[i] == answer[i+1]:
            cnt += 1
            continue
        result.append(cnt)
        cnt = 1
    result.append(cnt)
    return result