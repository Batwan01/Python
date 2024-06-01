# 1,000원을 신청한 부서에는 정확히 1,000원을 지원
#배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지
#d 부서별 신청한 금액, budget 예산
def solution(d, budget):
    count = 0
    sum = 0
    arr = []
    for num in sorted(d):
        if sum+num <= budget:
            sum+=num
            count+=1
    return count