def solution(n, m):
    num = 0
    a = n
    b = m
    while a != 0:
        num = b%a
        b = a
        a = num
    answer = [b,n*m/b]
    return answer