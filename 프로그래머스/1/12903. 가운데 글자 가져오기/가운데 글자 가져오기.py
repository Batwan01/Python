#s의 가운데 글자를 반환하는 함수
#길이가 짝수라면 가운데 두글자를 반환
def solution(s):
    
    return s[len(s)//2-1:len(s)//2+1] if len(s)%2==0 else s[len(s)//2]