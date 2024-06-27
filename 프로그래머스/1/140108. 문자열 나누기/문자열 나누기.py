#하나의 문자열을 여러 문자열로 분해
#x의 개수 = 다른 문자의 개수
def solution(s):
    count = 0
    flag = True
    arr = []
    for ch in s:
        if flag:
            x_count = 1
            another_count = 0
            x = ch
            flag = False
            continue
        
        if ch == x:
            x_count+=1
        else:
            another_count+=1
            
        if x_count == another_count:
            count+=1
            flag = True
            x = ""
    if x != "": count+=1
    return count