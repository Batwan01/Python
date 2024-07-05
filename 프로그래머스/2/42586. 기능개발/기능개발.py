import math
def solution(progresses, speeds):
    answer = []
    biggest = -math.inf

    for i in range(len(progresses)):
        time_to_done = math.ceil((100-progresses[i])/speeds[i])

        if biggest < time_to_done:
            biggest = time_to_done
            answer.append(1)

        else:
            answer[-1] += 1

    return answer