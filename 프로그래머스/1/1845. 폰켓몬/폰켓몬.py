#n마리 포켓몬 중 n/2가져가도 됨
#[3,1,2,3]이면 3번 포켓몬 2마리
#최대한 많은 종류의 포켓몬을 선택하려고 함
def solution(nums):
    count = len(nums)//2
    num_list = list(set(nums))
    if len(num_list) < count:
        answer = len(num_list)
    else:
        answer = count
    return answer