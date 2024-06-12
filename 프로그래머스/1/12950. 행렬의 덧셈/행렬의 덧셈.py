def solution(arr1, arr2):
    answer = []
    count = 0
    for num1,num2 in zip(arr1,arr2):
        sum = []
        for n1, n2 in zip(num1,num2):
            sum.append(n1+n2)
        answer.append(sum)
    return answer