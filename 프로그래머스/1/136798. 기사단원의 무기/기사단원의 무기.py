#기사에게 1번 부터 number까지 지정
#기사 번호의 약수 개수 = 공격력을 가진 무기
#만약 limit보다 크면 안됨
#공격력 1당 1kg
def solution(number, limit, power):
    answer = 0
    for num in range(1,number+1):
        count = 0
        middle = int(num**0.5)
        for i in range(1,middle+1):
            if num%i==0:
                if i**2==num:
                    count+=1
                else:
                    count+=2
            if count>limit:
                answer+=power
                break
        if count<=limit:
            answer+=count
                    
    return answer