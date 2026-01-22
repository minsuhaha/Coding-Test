def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    flag = False
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            flag = True
            return participant[i]
    
    if not flag:
        return participant[-1]
        
        