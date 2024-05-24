#두 정수 left와 right가 매개변수로 주어진다
#left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수 return
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        count = 0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count%2 == 0:
            answer+=i
        else:
            answer-=i
    return answer