
def solution(name, yearning, photo):
    answer = []
    dict = {}
    for ch,num in zip(name,yearning):
        dict[ch] = num
    
    for photo_list in photo:
        sum = 0
        for photo_name in photo_list:
            if photo_name in dict:
                sum += dict[photo_name]
        answer.append(sum)
    return answer