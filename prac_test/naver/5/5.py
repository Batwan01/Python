def solution(N):
    arr = []
    dict_num = {}
    count = 0
    
    for i in range(N):
        arr.append(input().split())
        dict_num[i] = abs(int(arr[-1][0]) - int(arr[-1][1]))
    dict_num = dict(sorted(dict_num.items(), key=lambda item: item[1]))
    
    schedule = []
    for i in dict_num:
        com_arr = []
        if len(schedule)==0:
            count += 1
            for num in range(int(arr[i][0]),int(arr[i][1])+1):
                schedule.append(num)
        else:
            for com_i in range(int(arr[i][0]),int(arr[i][1])+1):
                if com_i in schedule:
                    com_arr = []
                    break
                else:
                    com_arr.append(com_i)
            if len(com_arr) != 0:
                schedule.extend(com_arr)
                count+=1
    return count

print(solution(7))