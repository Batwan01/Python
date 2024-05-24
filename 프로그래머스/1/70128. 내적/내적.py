#정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적

def solution(a, b):
    return sum([num_1*num_2 for num_1, num_2 in zip(a,b)])