#n인 정사각형 배열 형태 -> "공백"(" ") 또는 "벽"("#") 두 종류
#지도 두개를 겹쳐서 하나라도 #가 있으면 벽, 둘다 공백이면 공백
# 벽은 1 공백은 0
def solution(n, arr1, arr2):
    arr = []
    for ar1,ar2 in zip(arr1, arr2):
        ar1 = bin(ar1)
        ar2 = bin(ar2)
        arr.append(bin(ar1&ar2))
    return arr
solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])

