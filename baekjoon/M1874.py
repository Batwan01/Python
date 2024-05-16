import sys
input = sys.stdin.readline

stack = []
answer = []
input_num = []
flag = False
N = int(input())

for i in range(N):
    input_num.append(int(input()))
    
count = 0
for i in range(1,N+1):
    stack.append(i)

    if stack[-1] == input_num[count]:
        stack.pop()
        answer.append('+')
        answer.append('-')
        # print("+")
        # print("-")
        count+=1
    else:
        # print("+")
        answer.append('+')
    while len(stack)!=0 and stack[-1] == input_num[count]:
        stack.pop()
        answer.append('-')
        # print("-")
        count+=1
        
if len(stack)!=0:
    print("NO")
else:
    for num in answer:
        print(num)