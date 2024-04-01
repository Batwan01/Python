K = int(input())

array = []
for i in range(K):
    N = int(input())
    if N != 0:
        array.append(N)
    else:
        del array[-1]

print(sum(array))