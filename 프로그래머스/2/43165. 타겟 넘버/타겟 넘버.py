# def solution(numbers, target):
#     answer = 0
    
#     def dfs(idx, total):
#         nonlocal answer
        
#         if idx == len(numbers):
#             if total == target:
#                 answer+=1
#             return
        
#         dfs(idx+1, total+numbers[idx])
#         dfs(idx+1, total-numbers[idx])
        
#     dfs(0,0)
#     return answer

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0,0))
    
    while queue:
        idx, total = queue.popleft()
        if idx == len(numbers):
            if total == target:
                answer+=1
        else:
            queue.append((idx+1, total+numbers[idx]))
            queue.append((idx+1, total-numbers[idx]))
            
    return answer