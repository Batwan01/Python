#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환
def solution(arr, divisor):
    arr.sort()
    answer = [num for num in arr if num%divisor==0]
    return answer if len(answer) else [-1]