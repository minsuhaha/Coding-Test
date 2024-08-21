def solution(players, callings):
    players_dict = {}
    for idx, player in enumerate(players):
        players_dict[player] = idx
    
    for calling in callings:
        curr_player = players_dict[calling] # 이름 불린 선수의 현재 등수 인덱스
        prior_player = players[curr_player-1] # 한 칸 앞에 있는 선수
        players[curr_player], players[curr_player-1] = players[curr_player-1], players[curr_player]
        players_dict[calling] -= 1
        players_dict[prior_player] += 1
    
    return players
    