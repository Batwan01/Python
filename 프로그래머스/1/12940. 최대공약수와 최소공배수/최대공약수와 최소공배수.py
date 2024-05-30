def solution(n, m):
    answer = []
    num = 0
    a = n
    b = m
    while a != 0:
        num = b%a
        b = a
        a = num
    answer.append(b)
    answer.append(n*m/b)
    return answer