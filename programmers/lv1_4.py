#11시 4분 -> 8분
#N의 각 자릿수의 합을 구해서 return 하는 solution 함수
#N = 123이면 1 + 2 + 3 = 6

def solution(n):
    return sum([int(num) for num in list(str(n))])