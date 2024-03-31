T = int(input())

for i in range(T):
    K = int(input())
    N = int(input())
    array = [num for num in range(N+1)]
    next_array = [0] * (N+1)

    for j in range(K):
        for k in range(1,N+1):
            next_array[k] = sum(array[0:k+1])
        array = next_array.copy()
    print(array[N])
