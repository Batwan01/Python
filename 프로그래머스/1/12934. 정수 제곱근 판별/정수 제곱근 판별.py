#n이 어떤 양의 정수 x의 제곱인지 아닌지 판단
#n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴
#n이 양의 정수 x의 제곱이 아니라면 -1
import math

def solution(n):
    if int(math.sqrt(n))-math.sqrt(n) == 0:
        print(n)
        answer = int(pow(math.sqrt(n)+1,2))
    else:
        answer = -1
    return answer