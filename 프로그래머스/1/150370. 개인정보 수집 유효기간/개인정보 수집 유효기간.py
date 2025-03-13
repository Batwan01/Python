# 1년 336
# 1달 28

def solution(today, terms, privacies):
    answer = []
    dict = {}
    
    year, month, day = today.split('.')
    today_date = int(year)*336 + int(month)*28 + int(day)
    
    for term in terms:
        alp, date = term.split()
        dict[alp] = int(date)
        
    for i, privacie in enumerate(privacies):
        date, alp = privacie.split()
        year, month, day = date.split('.')
        expiration = int(year)*336 + int(month)*28 + int(day)
        
        if expiration - today_date + dict[alp]*28 <= 0:
            answer.append(i+1)
            
    return answer