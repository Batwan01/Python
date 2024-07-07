from collections import deque
def solution(arr):
    que_arr = deque(arr)
    answer = []
    while len(que_arr) != 0:
        num = que_arr.popleft()
        if len(answer) == 0: answer.append(num)
        elif answer[-1] != num: answer.append(num)
    return answer