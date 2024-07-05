from collections import deque

def solution(priorities, location):
    que = deque((i,que) for i, que in enumerate(priorities))
    num = 0
    count = 0
    while que:
        num = que.popleft()
        if any(num[1] < que_num[1] for que_num in que):
            que.append(num)
        else:
            count+=1
            if num[0]==location: return count
    return -1