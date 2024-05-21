#0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어짐
#numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
def solution(numbers):
    # answer = sum([num for num in numbers if num not in range(10)])
    arr = set(range(10))
    answer = sum(arr - set(numbers))
    return answer