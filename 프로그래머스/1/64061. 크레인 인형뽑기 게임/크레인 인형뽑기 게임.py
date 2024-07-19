from collections import deque

def solution(board, moves):
    que = [deque(col) for col in zip(*board)]
    basket = deque()
    count = 0
    
    for num in moves:
        col_index = num - 1
        doll = 0
        
        while que[col_index]:
            doll = que[col_index].popleft()
            if doll != 0:
                break
        
        if doll == 0:
            if que[0] and que[0][0] != 0:
                doll = que[0].popleft()
            else:
                continue
        
        basket.append(doll)
        
        while len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            count += 2
            
    return count
