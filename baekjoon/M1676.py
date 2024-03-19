def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)

N = int(input())
str_N = str(factorial(N))
count = 0
for i in range(len(str_N)-1,-1,-1):
    if str_N[i] == '0':
        count+=1
    else:
        break

print(count)