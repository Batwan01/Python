def solution(schedules, timelogs, startday):
    answer = 0
    day = startday
    
    for schedule, timelog in zip(schedules, timelogs):
        count = 0
        for log in timelog:
            if day == 6 or day == 7 or (log//100 * 60 + log%100) - (schedule//100 * 60 + schedule%100) > 10:
                print(log - schedule)
                if day == 7: day = 1
                else: day+=1
            else:
                day+=1
                count+=1
        if count >= 5: answer+=1
    return answer


# 1은 월요일, 2는 화요일, 3은 수요일, 4는 목요일, 5는 금요일, 6은 토요일, 7은 일요일
