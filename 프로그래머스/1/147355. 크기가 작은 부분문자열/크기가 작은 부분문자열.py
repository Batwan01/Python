#t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열
#p가 나타내는 수보다 작거나 같은 것이 나오는 횟수
def solution(t, p):
    count = 0
    for i in range(len(t) - len(p)+ 1):
        arr_n = int(t[i:i+len(p)])
        if arr_n <= int(p):
            count+=1
    return count