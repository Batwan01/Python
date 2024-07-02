#5시 > 5시 10분
#알아볼 수 없느 번호 : 0
#순서 상관 X
#2~6개 일치부터  당첨 1~5순위
#lottos : 구매한 로또 번호, win_nums : 당첨 번호
#중복 없음, 1~45값
#최고, 최저 구하기
def solution(lottos, win_nums):
    dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    correct_count = 0
    zero_count = 0
    answer = []
    for num in lottos:
        if num in win_nums:
            correct_count+=1
        elif num == 0:
            zero_count+=1
    
    answer.append(dict[correct_count+zero_count])
    answer.append(dict[correct_count])
    return answer