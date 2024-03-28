import sys
input = sys.stdin.readline

array = []

N = int(input())
for i in range(N):
    array.append(list(map(int, input().split())))

array = sorted(array, key=lambda x: (x[0], x[1]))
for i in array:
    print(i[0], i[1])