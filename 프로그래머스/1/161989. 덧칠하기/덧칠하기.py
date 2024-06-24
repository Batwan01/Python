#n미터인 벽이 있다.
#1미터 구역을 n개로 나누고, 1~n번까지 번호 붙임
#벽을 칠하는 롤러의 길이 m
def solution(n, m, section):
    length = 0
    count = 1
    before = section[-1]
    for num in section[::-1]:
        length+= before - num
        before = num
            
        if length>=m:
            length = 0
            count +=1            
    #if length!=0: count+=1
    return count