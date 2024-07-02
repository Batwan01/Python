
def solution(N, K, S):
    num_arr = S.split()

    change_num = []
    count = {}
    for num in num_arr:
        change_num.append(bin(int(num))[2:])
    for num, num_2 in zip(num_arr,change_num):
        count[num] = num_2.count("1")

    answer_arr = list(sorted(count.items(), key=lambda item: (item[1],int(item[0])) ,reverse=True))
    print(answer_arr)
    return answer_arr[K-1][0]

print(solution(7,1, "1 2 4 8 16 32 64"))