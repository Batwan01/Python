#세 차례 던져 합계로 겨루는 게임
#0~10점,  Single(S), Double(D), Triple(T)은 1제곱, 2제곱, 3제곱이다.
#스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다.
#아차상(#) 당첨 시 해당 점수는 마이너스
#스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다
#스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다.
#Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재
#스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
def solution(dartResult):
    arr = []
    dict_pow = {"S":1,"D":2,"T":3}
    num = 0
    flag = False
    for ch in dartResult:
        if ch == "0" and num == 1:
            num = 10
            continue
        if ch.isdigit():
            num = int(ch)
            continue
        elif ch in dict_pow:
            num = pow(num,dict_pow[ch])
            arr.append(num)
        elif ch == "*":
            if len(arr) == 1:
                arr[len(arr)-1]*=2
            else:
                arr[len(arr)-1]*=2
                arr[len(arr)-2]*=2
        elif ch == "#":
            arr[len(arr)-1]*=-1
    return sum(arr)