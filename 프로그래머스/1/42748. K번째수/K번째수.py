# i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때 k 번째 값 구하기
# [1, 2, 3, 4, 5] -> 2,5,3 -> [2,3,4,5] 정렬 -> 4
def solution(array, commands):
    answer = []
    arr = []
    for ar in commands:
        arr = sorted(array[ar[0]-1:ar[1]])
        answer.append(arr[ar[2]-1])
    return answer