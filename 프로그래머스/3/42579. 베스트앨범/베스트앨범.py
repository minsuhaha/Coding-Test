from collections import defaultdict

def solution(genres, plays):
    genres_count = defaultdict(int)
    genres_lst = defaultdict(list)
    
    for i in range(len(genres)):
        genres_count[genres[i]] += plays[i]
        genres_lst[genres[i]].append((plays[i], i))
    
    sorted_genres_count = sorted(genres_count.items(), key=lambda x:x[1], reverse=True)
    
    answer = []
    for genre in sorted_genres_count:
        sorted_genres = sorted(genres_lst[genre[0]], key=lambda x:(-x[0], x[1]))
        for g in sorted_genres[:2]:
            answer.append(g[1])
    
    return answer