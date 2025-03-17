def solution(bandage, health, attacks):
    answer = health # 현재 체력

    for i in range(len(attacks) - 1):
        
        answer-=attacks[i][1]
        if answer <= 0: return -1
    
        attack_gap = attacks[i + 1][0] - attacks[i][0]
        if attack_gap <= 1: continue
        elif attack_gap > bandage[0]:
            if attack_gap//bandage[0] >= 1:
                answer+= (attack_gap-1)*bandage[1] + bandage[2] * (attack_gap//bandage[0])
            else:
                answer+= (attack_gap-1)*bandage[1] + bandage[2]
        else:
            answer+= (attack_gap-1)*bandage[1]
            
        if answer > health: answer = health

    answer-=attacks[-1][1]
    if answer <=0 : return -1
    return answer