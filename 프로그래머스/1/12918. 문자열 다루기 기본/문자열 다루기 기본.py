#s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수
def solution(s):
    return True if (len(s)==4 or len(s)==6) and s.isdigit() else False