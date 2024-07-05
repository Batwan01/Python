from collections import deque
def solution(prices):
    que = deque(prices)
    answer = []
    price = 0
    time = 0
    
    while que:
        price = que.popleft()
        if not que:
            answer.append(0)
            break
        time = 0
        for i,num in enumerate(que):
            if price <= num: continue
            else: break
        answer.append(i+1)
    return answer