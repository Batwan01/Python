#주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측
#짝수라면 x//2, 홀수라면 3x+1
#1 나올 때 까지 반복

def solution(num):
    count = 0
    while num!=1:
        if num%2==0:
            num//=2
        elif num%2==1:
            num = num*3+1
        count+=1
        if count==500:
            count=-1
            break
    return count