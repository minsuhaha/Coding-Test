from collections import defaultdict
def solution(genres, plays):
    genres_rank = defaultdict(int)
    for g, p in zip(genres, plays):
        genres_rank[g] += p
        
    answer = []
    idx = 0
    for g, p in zip(genres, plays):
        answer.append((genres_rank[g], p, idx))
        idx += 1
    answer.sort(key=lambda x:(-x[0], -x[1], x[2]))
    
    cnt = 1
    prior = answer[0][0]
    n_answer = [answer[0][2]]
    for a in answer[1:]:
        if a[0] == prior:
            if cnt == 2:
                continue
            else:
                cnt += 1
                n_answer.append(a[2])
        else:
            cnt = 1
            prior = a[0]
            n_answer.append(a[2])
    return n_answer