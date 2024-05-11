import sys
input = sys.stdin.readline

MAX = 0
NUM = 0
arr = []
count = []
flag = False
N = int(input())
for i in range(N):
    arr.append(int(input()))

arr.sort()
count = set(arr)
print(int(round(sum(arr) / N,0)))

print(arr[N//2])
for num in count:
    if arr.count(num)>MAX:
        MAX = arr.count(num)
        NUM = num
for num in count:
    if MAX == arr.count(num) and flag == False:
        flag = True
    elif MAX == arr.count(num) and flag == True:
        flag = 2
        print(num)
        break
if flag != 2:
    print(NUM)
print(abs(max(arr)-min(arr)))
