
def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name,yearning))
    for photo_list in photo:
        sum = 0
        for photo_name in photo_list:
            if photo_name in dic:
                sum += dic[photo_name]
        answer.append(sum)
    return answer