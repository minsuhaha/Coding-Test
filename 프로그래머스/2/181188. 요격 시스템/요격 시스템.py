def solution(targets):
    targets.sort(key=lambda x : x[1])
    start, end = targets[0][0], targets[0][1]
    cnt = 1
    for i in range(1, len(targets)):
        if end <= targets[i][0]:
            end = targets[i][1]
            cnt += 1
    
    return cnt
    