#정수들의 절댓값을 차례대로 담은 정수 배열 absolutes
#정수들의 부호를 차례대로 담은 불리언 배열 signs
#실제 정수들의 합
def solution(absolutes, signs):
    signs_conv = [1 if i else -1 for i in signs]
    return sum([abs_num*signs_num for abs_num, signs_num in zip(absolutes,signs_conv)])