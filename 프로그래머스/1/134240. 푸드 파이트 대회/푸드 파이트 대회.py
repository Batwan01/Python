#선수들은 1대 1로 대결하며, 매 대결마다 음식의 종류와 양이 바뀝니다
#일렬로 배치, 한 선수는 왼쪽 -> 오른쪽, 다른 선수는 오른쪽 -> 왼쪽 - 중앙에는 물이 있음 물 먹으면 승리
#칼로리가 낮은 음식을 먼저 먹는다.
#준비한 음식의 양을 칼로리가 적은 순서대로 나타내는 정수 배열 food가 주어졌을 때, 대회를 위한 음식의 배치를 나타내는 문자열
def solution(food):
    arr = []
    for i in range(1,len(food)):
        if food[i] // 2 >= 1:
            arr.append(str(i) * (food[i]//2))
    
    arr = ''.join(arr)
    answer = arr + '0' + arr[::-1]
    return answer