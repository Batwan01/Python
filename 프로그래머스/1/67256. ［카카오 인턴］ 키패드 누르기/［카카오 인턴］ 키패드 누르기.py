def solution(numbers, hand):
    answer = ''
    dict = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2),
        '*': (3,0), 0: (3,1), '#': (3,2)
    }
    
    left, right = dict['*'], dict['#'],

    for num in numbers:
        if dict[num][1] == 1:
            left_len = abs(left[0] - dict[num][0]) + abs(left[1] - dict[num][1])
            right_len = abs(right[0] - dict[num][0]) + abs(right[1] - dict[num][1])

            if left_len == right_len:
                if hand == 'right':
                    answer+="R"
                    right = dict[num]
                else:
                    answer+="L"
                    left = dict[num]
            elif left_len > right_len:
                answer+="R"
                right = dict[num]
            elif left_len < right_len:
                answer+="L"
                left = dict[num]
                
        elif dict[num][1] == 0:
            answer+="L"
            left = dict[num]
        elif dict[num][1] == 2:
            answer+="R"
            right = dict[num]
            
    return answer