#1~n 소수 찾기
def solution(n):
    count = 0
    for num in range(2,n+1):
        divisor = 0
        sqrt = int(num**0.5)
        for i in range(1,sqrt+1):
            if num%i == 0:
                divisor+=2
                if divisor>2:
                    break
        if divisor<3:
            count+=1
    return count