#원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기함
#이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상
#놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지, 부족하지 않으면 0
def solution(price, money, count):
    return count*(price+count*price)//2 - money if money - count*(price+count*price)//2<0 else 0