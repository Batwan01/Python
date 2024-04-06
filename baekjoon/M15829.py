import sys
input = sys.stdin.readline

N = int(input())
L = input()

sum = 0

# a : 97
for i in range(N):
    sum += (ord(L[i])-96)*pow(31,i)
print(sum)