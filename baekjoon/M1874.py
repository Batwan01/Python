stack = []
answer = []
input_num = []
flag = False
N = int(input())

for i in range(N):
    input_num.append(int(input()))

count = 0
while N < count:
    for i in range(1,N+1):
        if i < input_num[count]:
            answer.append(i)
            count+=1
        elif i == input_num[count]:
            answer.append(i)
            count+=1