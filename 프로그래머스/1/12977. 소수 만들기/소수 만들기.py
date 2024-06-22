#3개의 수가 더해졌을 때 소수 개수
def solution(nums):
    num_sum = 0
    count = 0
    arr = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for h in range(j+1, len(nums)):
                arr.append(nums[i]+nums[j]+nums[h])
    
    
    for num in arr:
        check = 0
        sqrt = int(num**0.5)
        for divisor in range(1,sqrt+1):
            if num%divisor == 0:
                check += 2
                if check>2:
                    break
        if check<3:
            count+=1
                
    return count




