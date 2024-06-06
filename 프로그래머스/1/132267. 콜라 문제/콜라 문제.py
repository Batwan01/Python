#빈 병 2개면 콜라 1병을 줌
#20 -> 10 -> 5 -> 2 -> 1 + (아까 남은 1개) -> 1 = 19병
#a개 빈병 -> b병, 빈병 개수 : n
def solution(a, b, n):
    have = n
    count = 0
    while have>=a:
        count += have//a*b
        have = have%a + have//a*b
    return count