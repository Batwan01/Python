#a와 b 사이에 속한 모든 정수의 합을 리턴
def solution(a, b):
    return sum(i for i in range(min(a,b),max(a,b)+1))