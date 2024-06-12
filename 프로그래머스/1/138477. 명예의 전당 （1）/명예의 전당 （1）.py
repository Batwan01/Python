#점수 중 상위 k번째 이내면 명예의 전당
#K을 넘어가면 원래 k는 떨어짐
def solution(k, score):
    honor = []
    answer = []
    for num in score:
        if len(honor)<k:
            honor.append(num)
        elif num>min(honor):
            honor[honor.index(min(honor))] = num
        answer.append(min(honor))
    return answer