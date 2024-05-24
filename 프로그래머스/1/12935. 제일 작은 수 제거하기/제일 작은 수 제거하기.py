#arr 에서 가장 작은 수를 제거한 배열을 리턴
#빈 배열인 경우엔 배열에 -1을
#[10] -1을 리턴

def solution(arr):
    arr.remove(min(arr))
    return [-1] if not arr else arr