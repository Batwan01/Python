def solution(N, K, S):
    count = 0
    K_str = str(K)
    num_arr = S.split()
    for num in num_arr:
        #num_arr = [i for i in num]
        if K_str not in num: count+=1
    return count


print(solution(5,2,"10 20 22 12 11"))