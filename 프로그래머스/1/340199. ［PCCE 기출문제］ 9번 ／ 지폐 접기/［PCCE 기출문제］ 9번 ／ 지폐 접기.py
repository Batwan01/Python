# 14:00
# 항상 길이가 긴 쪽을 반으로 접습니다.
# 홀수였다면 접은 후 소수점 이하는 버립니다.
# 90도 돌려서 지갑에 넣을 수 있다면 그만 접습니다.
# 접어야 하는 최소 횟수

def solution(wallet, bill):
    answer = 0
    while True:
        if max(wallet) >= max(bill) and min(wallet) >= min(bill):
            break
        elif max(wallet) < max(bill):
            index = bill.index(max(bill))
            bill[index] = bill[index] // 2
            answer+=1
        elif min(wallet) < min(bill):
            index = bill.index(max(bill))
            bill[index] = bill[index] // 2
            answer+=1
    return answer