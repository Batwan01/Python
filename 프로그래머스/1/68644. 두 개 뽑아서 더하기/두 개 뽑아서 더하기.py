#numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        arr = [numbers[i] + numbers[j] for j in range(i+1,len(numbers))]
        answer.append(arr)
    return sorted(list(set(sum(answer,[]))))