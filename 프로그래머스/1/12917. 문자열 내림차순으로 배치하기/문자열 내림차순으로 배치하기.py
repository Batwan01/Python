#문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴
#대문자는 소문자보다 작은 것으로 간주
def solution(s):
    return ''.join(sorted(list(s),reverse=True))