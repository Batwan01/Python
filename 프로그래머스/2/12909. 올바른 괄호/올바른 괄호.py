from collections import deque
def solution(s):
    answer = True
    open_ch = deque()
    que_ch = ""
    que = deque(s)
    flag = False
    
    while que:
        ch = que.popleft()
        if ch == ")":
            if open_ch and open_ch.pop() == "(":continue
            else:
                flag = True
                break
        else:
            open_ch.append(ch)

    if flag or open_ch: return False
    else: return True