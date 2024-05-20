#n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return
def solution(n):
    return min(i for i in range(1,n) if n%i==1)