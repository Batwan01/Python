def solution(bandage, health, attacks):
    answer = health  # 현재 체력

    for i in range(len(attacks) - 1):
        # 공격 받기
        answer -= attacks[i][1]
        if answer <= 0: 
            return -1  # 체력이 0 이하가 되면 즉시 종료

        attack_gap = attacks[i + 1][0] - attacks[i][0]
        if attack_gap <= 1: 
            continue  # 연속 성공 시간이 1초 이하이면 회복할 필요 없음
        else:
            full_cycles = (attack_gap - 1) // bandage[0]  # 연속 성공 횟수
            remaining_time = (attack_gap - 1) % bandage[0]  # 남은 시간
            
            # 기본 회복량 + 연속 성공 시 추가 회복
            answer += (attack_gap - 1) * bandage[1] + full_cycles * bandage[2]

        # 최대 체력 초과 방지
        if answer > health: 
            answer = health

    # 마지막 공격 처리
    answer -= attacks[-1][1]
    if answer <= 0: 
        return -1

    return answer
