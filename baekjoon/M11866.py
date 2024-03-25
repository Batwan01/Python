N, K = map(int, input().split())

array = []
for i in range(1,N+1):
    array.append(i)

for i in range(N):
    print((K-1)%len(array)+1)
# for i in range(N):
#     print(array)
#     del array[K-1]
#     K+=3
#     if K-1>len(array):
#         K = abs(K-N)