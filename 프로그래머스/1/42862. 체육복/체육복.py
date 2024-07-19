def solution(n, lost, reserve):
    # 여분이 있지만 잃어버린 학생을 먼저 처리합니다.
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    answer = n - len(lost_set)
    
    for num in sorted(lost_set):
        if num - 1 in reserve_set:
            reserve_set.remove(num - 1)
            answer += 1
        elif num + 1 in reserve_set:
            reserve_set.remove(num + 1)
            answer += 1
    
    return answer