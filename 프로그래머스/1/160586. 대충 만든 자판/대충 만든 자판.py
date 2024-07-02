#딕셔너리 두개를 합칠 예정

def solution(keymap, targets):
    dict = {}
    for ch_arr in keymap:
        count = 0
        for i, ch in enumerate(ch_arr):
            if ch not in dict:
                dict[ch] = i+1
            elif dict[ch] > i:
                dict[ch] = i+1
                
    arr = []
    for ch_arr in targets:
        answer_count = 0
        for ch in ch_arr:
            if ch not in dict:
                answer_count = -1
                break
            answer_count += dict[ch]
        arr.append(answer_count)
    return arr