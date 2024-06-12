#일정한 거리만큼 밀어서 다른 알파벳으로 바꾸기
#"AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"
def solution(s, n):
    arr = []
    for i in range(len(s)):
        if s[i] == ' ':
            arr.append(' ')
        else:
            if ord(s[i])>=65 and ord(s[i])<=90:
                if ord(s[i])+n>90:
                    arr.append(chr(64+ord(s[i])+n-90))
                else:
                    arr.append(chr(ord(s[i])+n))
                    
            if ord(s[i])>=97 and ord(s[i])<=122:
                if ord(s[i])+n>122:
                    arr.append(chr(96+ord(s[i])+n-122))
                else:
                    arr.append(chr(ord(s[i])+n))
    return ''.join(arr)

