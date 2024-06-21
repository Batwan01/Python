#과일 상태에 따라 1~k
#m개씩 담아 포장 가격은 상자의 가장 낮은 점수 * m
#k는 최대 점수, m은 사장에 담을 개수, score은 각각의 점수
def solution(k, m, score):
    score.sort(reverse=True)
    group = [score[i:i+m] for i in range(0,len(score),m) if len(score)>=i+m]
    price = 0
    for group_list in group:
        min_num = min(group_list)
        if min_num>k: min_num=k
        price += min_num*m
    return price