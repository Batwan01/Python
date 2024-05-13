stack = []
answer = []

N = int(input())

for i in range(1,N+1):
    answer.append(i)
    stack.append(int(input()))

print(answer,stack)