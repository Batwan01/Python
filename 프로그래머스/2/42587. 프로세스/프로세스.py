from collections import deque
def solution(priorities, location):
    count = 0
    que_num = 0
    que = deque((priority, i) for i, priority in enumerate(priorities))
    
    while que:
        que_num = que.popleft()
        
        if any(que_num[0]<other[0] for other in que):
            que.append(que_num)
        else:
            count+=1
            if que_num[1] == location:
                return count
    return -1