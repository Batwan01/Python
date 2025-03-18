def solution(id_list, report, k):
    answer = []
    
    dict_id = {}
    dict_report = {}
    for id in id_list:
        dict_id[id] = []
        dict_report[id] = 0
        
    for r in report:
        user, r_user = r.split()
        if user not in dict_id[r_user]: dict_id[r_user].append(user)
        # if r_user not in dict_report[user]: dict_report[user].append(r_user)
        

    for id in id_list:
        if len(dict_id[id]) >= k:
            for user in dict_id[id]:
                dict_report[user]+=1
                
    for r in dict_report:
        answer.append(dict_report[r])
    return answer