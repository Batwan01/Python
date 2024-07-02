from collections import deque

def solution(S):
    arr_words = list(S.split(" "))
    compare = []
    for arr_word in arr_words:
        arr = deque()
        st = ""
        for ch in arr_word:
            if ch.isdigit():
                st+=ch
            else:
                arr.append(st)
                arr.append(ch)
                st = ""
        if st!="": arr.append(st)
    
        answer = deque()
        while len(arr)!=0:
            pop_word = arr.popleft()
            if pop_word.isdigit():
                answer.append(int(pop_word))
            elif pop_word=="%":
                answer.append(answer.pop()%int(arr.popleft()))
            elif pop_word=="*":
                answer.append(answer.pop()*int(arr.popleft()))
            else:
                answer.append(pop_word)
        print(answer)
        while len(answer) != 1:
            first_num = answer.popleft()
            option = answer.popleft()
            second_num = answer.popleft()
            if option=="+":
                answer.appendleft(first_num+second_num)
            elif option=="-":
                answer.appendleft(first_num-second_num)
        compare.append(answer.pop())
    return max(compare)

print(solution("10*10-99 99-10*10"))





# for arr_word in arr_words:
#     arr = deque()
#     st = ""
#     for ch in arr_word:
#         if ch.isdigit():
#             st+=ch
#         else:
#             arr.append(st)
#             arr.append(ch)
#             st = ""
#     if st!="": arr.append(st)

#     num_arr = deque()
#     other_arr = deque()
#     while len(arr)!=0:
#         pop_word = arr.popleft()
#         if pop_word.isdigit():
#             num_arr.append(pop_word)
#         elif pop_word=="*" or pop_word=="%":
            
#         else:


# 10 * 3 + 2

# 2 3
# +

# 3 * 10

