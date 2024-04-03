import sys
input = sys.stdin.readline

N = int(input())
check = True
for i in range(N):
    str_i = str(i)
    int_i = [int(char) for char in str_i]
    sum_i = sum(int_i)
    if N == i + sum_i:
        print(i)
        check = False
        break
if check:
    print(0)