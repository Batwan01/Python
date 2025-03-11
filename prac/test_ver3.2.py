def solution(v):
    answer = []
    v_row = v.pop()
    compare = v.pop()

    if v_row[0] == compare[0]:
        answer.append(v[0][0])
    else:
        if v_row[0] == v[0][0]:
            answer.append(compare[0])
        else:
            answer.append(v_row[0])
        
    if v_row[1] == compare[1]:
        answer.append(v[0][1])
    else:
        if v_row[1] == v[0][1]:
            answer.append(compare[1])
        else:
            answer.append(v_row[1])
            
    return answer