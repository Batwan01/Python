def solution(answers):
    method = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    answer_count = {}
    answer = []
    person_num = 0
    max_count = 0
    for arr in method:
        person_num+=1
        index = 0
        count = 0
        for ans_num in answers:
            if ans_num == arr[index%len(arr)]:
                count+=1
            index+=1
            
        answer_count[person_num] = count
        if max_count<count:
            max_count = count
    
    answer = [num for num, count in answer_count.items() if count==max_count]
    return answer