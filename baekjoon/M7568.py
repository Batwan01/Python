import sys
input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append(list(map(int,input().split())))
    array[i].append(1)

for i in range(N):
    for j in range(N):        
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            array[i][2]+=1

for i in range(N):
    print(array[i][2], end = ' ')