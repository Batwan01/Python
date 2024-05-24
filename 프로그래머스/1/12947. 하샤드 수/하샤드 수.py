#4:36 ->
#x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 함
#18의 자릿수 합 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수
def solution(x):
    
    return True if x%sum(list(map(int,str(x))))==0 else False