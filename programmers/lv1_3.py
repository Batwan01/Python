#9시 44분 ->
#n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수

def solution(n):
    sum_n = 0
    for i in range(1,n+1):
        if n%i == 0:
            sum_n+=i
    return sum_n


