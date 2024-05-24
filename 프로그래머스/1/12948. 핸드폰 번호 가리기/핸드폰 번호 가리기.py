#문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴
def solution(phone_number):
    answer = list(phone_number)
    answer[:-4] = ['*'] * (len(phone_number)-4)
    answer = ''.join(answer)
    return answer