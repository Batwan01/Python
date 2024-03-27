import sys
input = sys.stdin.readline

N = int(input())

array = []
instruct = []
for i in range(N):
    instruct = list(map(str,input().split()))
    if instruct[0] == 'push':
        array.append(instruct[1])
    elif instruct[0] == 'pop':
        if len(array) == 0:
            print('-1')
        else:
            print(array.pop())
    elif instruct[0] == 'size':
        print(len(array))
    elif instruct[0] == 'empty':
        if len(array) == 0:
            print('1')
        else:
            print('0')
    elif instruct[0] == 'top':
        if len(array) == 0:
            print('-1')
        else:
            print(array[-1])