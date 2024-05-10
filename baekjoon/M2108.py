import sys
input = sys.stdin.readline

arr = []
count = []
N = int(input())
for i in range(N):
    arr.append(int(input()))

count = set(arr)
print(arr, count)
arr.sort()
print(sum(arr) // N)
print(arr[N//2])

print(abs(max(arr)-min(arr)))
