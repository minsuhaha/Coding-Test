def solution(progresses, speeds):
    day = []
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        if remain % speeds[i] == 0:
            day.append(remain // speeds[i])
        else:
            day.append((remain // speeds[i])+1) 
    
    answer = []
    prior = day[0]
    cnt = 1
    for d in day[1:]:
        if d <= prior:
            cnt += 1
        else:
            answer.append(cnt)
            prior = d
            cnt = 1
    answer.append(cnt)
    return answer
        
    