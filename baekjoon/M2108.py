import sys
input = sys.stdin.readline
from collections import Counter

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

counter = Counter(arr)
counter = counter.most_common()
if len(counter) >1:
    if counter[0][1] == counter[1][1]:
        print(counter[1][0])
    else:
        print(counter[0][0])
else:
        print(counter[0][0])
    
print(abs(max(arr)-min(arr)))
