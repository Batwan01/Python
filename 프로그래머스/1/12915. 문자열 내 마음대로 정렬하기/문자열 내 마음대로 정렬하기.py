#n번째 글자를 기준으로 오름차순 정렬

def solution(strings, n):
    strings.sort(key = lambda x:(x[n],x))
    return strings