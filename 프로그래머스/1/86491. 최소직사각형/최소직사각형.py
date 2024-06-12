#가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑
#2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑
#가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어짐
#가장 작은 지갑을 만들기
def solution(sizes):
    column_1 = max(max(num) for num in sizes)
    column_2 = max(min(num) for num in sizes)
    return column_1 * column_2

