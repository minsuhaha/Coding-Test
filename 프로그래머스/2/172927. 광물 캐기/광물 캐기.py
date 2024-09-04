def solution(picks, minerals):
    minerals = minerals[:sum(picks)*5]
    minerals_group = []
    for i in range(0, len(minerals), 5):
        d_cnt, i_cnt, s_cnt = 0, 0, 0
        for mineral in minerals[i:i+5]:
            if mineral == 'diamond':
                d_cnt += 1
            elif mineral == 'iron':
                i_cnt += 1
            else:
                s_cnt += 1
        minerals_group.append((d_cnt, i_cnt, s_cnt))
    
    minerals_group.sort(key=lambda x:(x[0], x[1], x[2]))
    
    total = 0
    while minerals_group:
        if picks[0]:
            total += sum(minerals_group[-1])
            picks[0] = picks[0]-1
        elif picks[1]:
            total += (minerals_group[-1][0]*5 + minerals_group[-1][1] + minerals_group[-1][2])
            picks[1] = picks[1]-1
        elif picks[2]:
            total += (minerals_group[-1][0]*25 + minerals_group[-1][1]*5 + minerals_group[-1][2])
            picks[2] = picks[2]-1    
        minerals_group.pop()

    return total