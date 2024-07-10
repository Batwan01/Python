from collections import Counter

def solution(X, Y):
    count_x = Counter(X)
    count_y = Counter(Y)
    
    common_counts = count_x & count_y
    
    if not common_counts:
        return "-1"
    
    result = []
    for num in sorted(common_counts.keys(), reverse=True):
        result.extend([num] * common_counts[num])
    
    answer = ''.join(result)
    
    if answer == "":
        return "-1"
    elif answer == "0" * len(answer):
        return "0"
    else:
        return answer
