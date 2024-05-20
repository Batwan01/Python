#9시 29분 시작 -> 34분 종료
#s에 'p'의 개수와 'y'의 개수 == True, != False를 return 하는 solution
#'p', 'y' 모두 하나도 없는 경우는 항상 True
#대문자와 소문자는 구별하지 않음
def solution(s):
    answer = True
    
    word = s.lower()
    if word.count('p') == word.count('y') or (word.count('p') == 0 and word.count('y') == 0):
        answer = True
    else:
        answer = False
    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))