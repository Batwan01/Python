#s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지
#s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행
#
def solution(s):
    arr = []
    answer = []
    for ch in s:
        if ch in arr:
            a = list(reversed(arr))
            answer.append(a.index(ch)+1)
        else:
            answer.append(-1)
        arr.append(ch)
    return answer