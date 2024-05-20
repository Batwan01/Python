#a와 b 사이에 속한 모든 정수의 합을 리턴
def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(i for i in range(a,b+1))