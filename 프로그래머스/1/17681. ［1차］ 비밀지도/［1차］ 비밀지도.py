#n인 정사각형 배열 형태 -> "공백"(" ") 또는 "벽"("#") 두 종류
#지도 두개를 겹쳐서 하나라도 #가 있으면 벽, 둘다 공백이면 공백
# 벽은 1 공백은 0
def solution(n, arr1, arr2):
    arr = []
    for ar1,ar2 in zip(arr1, arr2):
        num = bin(ar1|ar2)[2:]
        num = num.replace("1","#")
        num = num.replace("0"," ")
        arr.append(str(num).rjust(n,' '))
        
    return arr