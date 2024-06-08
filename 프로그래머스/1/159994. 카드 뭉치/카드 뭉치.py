def solution(cards1, cards2, goal):
    answer = []
    index1 = 0
    index2 = 0
    for ch in goal:
        if len(cards1)>index1 and cards1[index1] == ch:
            answer.append(cards1[index1])
            index1+=1
        elif len(cards2)>index2 and cards2[index2] == ch:
            answer.append(cards2[index2])
            index2+=1
        else:
            break
    if answer == goal:
        return "Yes"
    return "No"