def can_place_mat(park, x, y, size):
    """
    (x, y)에서 size x size 크기의 돗자리를 깔 수 있는지 확인하는 함수
    """
    if x + size > len(park) or y + size > len(park[0]):
        return False
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if park[i][j] != "-1":
                return False
    return True

def solution(mats, park):
    mats.sort(reverse=True)  # 큰 돗자리부터 확인
    
    for mat in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if can_place_mat(park, i, j, mat):
                    return mat
    
    return -1  # 깔 수 있는 돗자리가 없는 경우
