#seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"
#seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없다.
def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'