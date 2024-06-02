#단어는 하나 이상의 공백문자로 구분
#짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열
def solution(s):
    arr = s.split(' ')
    answer = []
    for word in arr:
        arr_word = []
        for i in range(len(word)):
            if i%2 == 0:
                arr_word.append(word[i].upper())
            else:
                arr_word.append(word[i].lower())
        arr_word = ''.join(arr_word)
        answer.append(arr_word)
    return ' '.join(answer)