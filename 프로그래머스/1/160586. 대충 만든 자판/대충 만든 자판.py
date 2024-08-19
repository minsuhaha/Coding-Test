def solution(keymap, targets):
    dict_keymap = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dict_keymap.keys():
                dict_keymap[key[i]] = i+1
                continue
            dict_keymap[key[i]] = min(dict_keymap[key[i]], i+1)
    
    answer = []
    for target in targets:
        cnt = 0
        for t in target:
            if t not in dict_keymap.keys():
                cnt = -1
                break
            cnt += dict_keymap[t]
        answer.append(cnt)
    return answer