#실패율 = 스테이지 도달했지만 클리어하지 못 한 플레이어 수 / 스테이지에 도달한 플레이어 수
#N = 전체 스테이지의 개수, 현재 스테이지 담은 배열 stages
#실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 
def solution(N, stages):
    stages.sort()
    answer = []
    arr_len = len(stages)
    com_arr = set(stages)
    arr = {}
    for i in range(1,N+1):
        arr[i] = 0

    for num in com_arr:
        if num == N+1:
            if num-1 in stages:
                arr[num-1] = stages.count(num-1) / (len(stages) - stages.index(num-1))
            else:
                arr[num-1] = stages.count(num-1) / (len(stages) - stages.index(num))
        else:
            arr[num] = stages.count(num) / (len(stages) - stages.index(num))
    ans_arr = sorted(arr.items(), key=lambda item: item[1], reverse=True)
    for i in range(0,len(ans_arr)):
        answer.append(ans_arr[i][0])
    return answer