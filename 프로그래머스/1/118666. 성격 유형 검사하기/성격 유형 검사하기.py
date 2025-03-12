def solution(survey, choices):
    answer = ''
    dict_survey = dict.fromkeys(["R", "T", "C", "F", "J", "M", "A", "N"], 0)
    pairs = ["RT", "CF", "JM", "AN"]
    for word, score in zip(survey, choices):
        if score == 1:
            dict_survey[word[0]]+=3
        elif score == 2:
            dict_survey[word[0]]+=2
        elif score == 3 :
            dict_survey[word[0]]+=1
        elif score == 4:
            continue
        elif score == 5:
            dict_survey[word[1]]+=1
        elif score == 6:
            dict_survey[word[1]]+=2
        elif score == 7:
            dict_survey[word[1]]+=3
        else:
            continue
    
    for pair in pairs:
        ch1, ch2 = pair
        if dict_survey[ch1] >= dict_survey[ch2]: answer+=ch1
        else: answer+=ch2
        
    return answer